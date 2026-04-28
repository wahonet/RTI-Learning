#!/usr/bin/env python3
"""
Experimental enhancement pipeline for low-contrast stone inscription photos.

This is not a magic OCR model. It generates several diagnostic/enhanced views
that make shallow incisions easier for humans and downstream OCR models to see.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np


def imwrite(path: Path, image: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ok = cv2.imwrite(str(path), image)
    if not ok:
        raise RuntimeError(f"Failed to write {path}")


def normalize_u8(arr: np.ndarray, low: float = 1.0, high: float = 99.0) -> np.ndarray:
    arr = arr.astype(np.float32)
    lo, hi = np.percentile(arr, [low, high])
    if hi <= lo:
        hi = lo + 1.0
    out = (arr - lo) * 255.0 / (hi - lo)
    return np.clip(out, 0, 255).astype(np.uint8)


def resize_long_side(image: np.ndarray, max_long_side: int | None) -> tuple[np.ndarray, float]:
    if not max_long_side or max(image.shape[:2]) <= max_long_side:
        return image, 1.0
    h, w = image.shape[:2]
    scale = max_long_side / float(max(h, w))
    resized = cv2.resize(image, (round(w * scale), round(h * scale)), interpolation=cv2.INTER_AREA)
    return resized, scale


def remove_red_overlay(bgr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Mask and inpaint red/pink coordinate overlays often burned into survey photos."""
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 45, 80], dtype=np.uint8)
    upper_red1 = np.array([12, 255, 255], dtype=np.uint8)
    lower_red2 = np.array([165, 45, 80], dtype=np.uint8)
    upper_red2 = np.array([179, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)

    # Restrict to vivid red/pink pixels so natural stone browns survive.
    b, g, r = cv2.split(bgr)
    vivid = ((r.astype(np.int16) - g.astype(np.int16)) > 30) & ((r.astype(np.int16) - b.astype(np.int16)) > 25)
    mask = np.where(vivid, mask, 0).astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)
    inpainted = cv2.inpaint(bgr, mask, 5, cv2.INPAINT_TELEA)
    return inpainted, mask


def flatten_illumination(gray: np.ndarray, sigma: float) -> np.ndarray:
    """Remove slow lighting/shadow gradients by dividing by a blurred background."""
    gray_f = gray.astype(np.float32)
    background = cv2.GaussianBlur(gray_f, ksize=(0, 0), sigmaX=sigma, sigmaY=sigma)
    background = np.maximum(background, 1.0)
    flat = gray_f / background * np.mean(background)
    return normalize_u8(flat, 0.5, 99.5)


def clahe(gray: np.ndarray, clip_limit: float = 2.5, tile_grid_size: int = 12) -> np.ndarray:
    enhancer = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_grid_size, tile_grid_size))
    return enhancer.apply(gray)


def multiscale_unsharp(gray: np.ndarray) -> np.ndarray:
    gray_f = gray.astype(np.float32)
    detail = np.zeros_like(gray_f)
    for sigma, weight in [(1.2, 0.9), (2.5, 0.55), (6.0, 0.35)]:
        blur = cv2.GaussianBlur(gray_f, (0, 0), sigmaX=sigma, sigmaY=sigma)
        detail += weight * (gray_f - blur)
    boosted = gray_f + 1.4 * detail
    return normalize_u8(boosted, 0.5, 99.5)


def directional_gabor(gray: np.ndarray) -> np.ndarray:
    gray_f = gray.astype(np.float32) / 255.0
    responses = []
    for theta in np.linspace(0, np.pi, 8, endpoint=False):
        kernel = cv2.getGaborKernel((21, 21), sigma=4.0, theta=theta, lambd=10.0, gamma=0.35, psi=0)
        resp = cv2.filter2D(gray_f, cv2.CV_32F, kernel)
        responses.append(np.abs(resp))
    return normalize_u8(np.max(np.stack(responses, axis=0), axis=0), 1.0, 99.5)


def relief_from_gray(gray: np.ndarray, light: tuple[float, float, float]) -> np.ndarray:
    height = cv2.GaussianBlur(gray.astype(np.float32), (0, 0), 0.9) / 255.0
    gx = cv2.Scharr(height, cv2.CV_32F, 1, 0)
    gy = cv2.Scharr(height, cv2.CV_32F, 0, 1)
    normal = np.dstack((-gx, -gy, np.ones_like(height) * 0.55))
    normal /= np.maximum(np.linalg.norm(normal, axis=2, keepdims=True), 1e-6)
    light_vec = np.array(light, dtype=np.float32)
    light_vec /= np.linalg.norm(light_vec)
    shade = np.sum(normal * light_vec, axis=2)
    return normalize_u8(shade, 1.0, 99.0)


def morphology_views(gray: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Character strokes are tiny compared with the stone slab; test several scales.
    hats = []
    for size in [7, 11, 17, 25]:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
        blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
        tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
        hats.append(np.maximum(blackhat, tophat))
    stroke_energy = normalize_u8(np.max(np.stack(hats, axis=0), axis=0), 1.0, 99.5)

    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    adaptive = cv2.adaptiveThreshold(
        opened,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        41,
        7,
    )
    return stroke_energy, adaptive


def make_contact_sheet(items: list[tuple[str, np.ndarray]], width: int = 420) -> np.ndarray:
    tiles = []
    font = cv2.FONT_HERSHEY_SIMPLEX
    for label, img in items:
        if img.ndim == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        h, w = img.shape[:2]
        scale = width / float(w)
        tile = cv2.resize(img, (width, max(1, round(h * scale))), interpolation=cv2.INTER_AREA)
        header = np.full((34, width, 3), 245, dtype=np.uint8)
        cv2.putText(header, label, (10, 23), font, 0.55, (30, 30, 30), 1, cv2.LINE_AA)
        tiles.append(np.vstack([header, tile]))

    max_h = max(tile.shape[0] for tile in tiles)
    padded = []
    for tile in tiles:
        pad = max_h - tile.shape[0]
        if pad:
            tile = np.vstack([tile, np.full((pad, tile.shape[1], 3), 255, dtype=np.uint8)])
        padded.append(tile)

    rows = []
    for i in range(0, len(padded), 2):
        row_tiles = padded[i : i + 2]
        if len(row_tiles) == 1:
            row_tiles.append(np.full_like(row_tiles[0], 255))
        rows.append(np.hstack(row_tiles))
    return np.vstack(rows)


def crop_roi(image: np.ndarray, roi: list[int] | None) -> tuple[np.ndarray, list[int] | None]:
    if not roi:
        return image, None
    if len(roi) != 4:
        raise ValueError("--roi expects four integers: x y width height")
    x, y, w, h = roi
    ih, iw = image.shape[:2]
    x1 = max(0, min(iw - 1, x))
    y1 = max(0, min(ih - 1, y))
    x2 = max(x1 + 1, min(iw, x + w))
    y2 = max(y1 + 1, min(ih, y + h))
    return image[y1:y2, x1:x2].copy(), [x1, y1, x2 - x1, y2 - y1]


def process(input_path: Path, output_dir: Path, max_long_side: int | None, roi: list[int] | None = None) -> dict:
    bgr0 = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
    if bgr0 is None:
        raise FileNotFoundError(input_path)

    cropped, used_roi = crop_roi(bgr0, roi)
    bgr, scale = resize_long_side(cropped, max_long_side)
    no_overlay, red_mask = remove_red_overlay(bgr)
    gray = cv2.cvtColor(no_overlay, cv2.COLOR_BGR2GRAY)

    sigma = max(18.0, max(gray.shape[:2]) / 32.0)
    flat = flatten_illumination(gray, sigma=sigma)
    contrast = clahe(flat)
    sharp = multiscale_unsharp(contrast)
    gabor = directional_gabor(sharp)
    stroke_energy, adaptive = morphology_views(sharp)
    relief_ne = relief_from_gray(flat, (0.8, -0.6, 0.55))
    relief_sw = relief_from_gray(flat, (-0.8, 0.6, 0.55))

    # A compact OCR-oriented hint image: contrast in gray, stroke candidates in cyan/red.
    composite = cv2.cvtColor(contrast, cv2.COLOR_GRAY2BGR)
    composite[:, :, 1] = np.maximum(composite[:, :, 1], gabor)
    composite[:, :, 2] = np.maximum(composite[:, :, 2], stroke_energy)

    outputs = [
        ("00_input_resized.png", bgr),
        ("01_red_overlay_mask.png", red_mask),
        ("02_overlay_inpainted.png", no_overlay),
        ("03_gray.png", gray),
        ("04_illumination_flattened.png", flat),
        ("05_clahe_local_contrast.png", contrast),
        ("06_multiscale_unsharp.png", sharp),
        ("07_directional_gabor_strokes.png", gabor),
        ("08_morphological_stroke_energy.png", stroke_energy),
        ("09_relief_light_ne.png", relief_ne),
        ("10_relief_light_sw.png", relief_sw),
        ("11_adaptive_binary_candidate.png", adaptive),
        ("12_ocr_hint_composite.png", composite),
    ]

    for filename, image in outputs:
        imwrite(output_dir / filename, image)

    sheet_items = [
        ("input", bgr),
        ("inpainted", no_overlay),
        ("flat", flat),
        ("clahe", contrast),
        ("gabor", gabor),
        ("stroke energy", stroke_energy),
        ("relief NE", relief_ne),
        ("binary candidate", adaptive),
    ]
    contact = make_contact_sheet(sheet_items)
    imwrite(output_dir / "contact_sheet.jpg", contact)

    manifest = {
        "input": str(input_path),
        "output_dir": str(output_dir),
        "original_shape_hwc": list(bgr0.shape),
        "roi_xywh_original_pixels": used_roi,
        "processed_shape_hwc": list(bgr.shape),
        "resize_scale": scale,
        "illumination_sigma": sigma,
        "note": "Inspect relief and stroke-energy images by zooming in; do not treat binary output as ground truth.",
        "files": [name for name, _ in outputs] + ["contact_sheet.jpg"],
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Path to an inscription photo")
    parser.add_argument("-o", "--output-dir", type=Path, default=Path("outputs/stele_enhance"))
    parser.add_argument("--max-long-side", type=int, default=2600, help="Resize long side for faster experiments; 0 keeps full size")
    parser.add_argument("--roi", type=int, nargs=4, metavar=("X", "Y", "W", "H"), help="Optional crop in original image pixels")
    args = parser.parse_args()
    max_long_side = None if args.max_long_side == 0 else args.max_long_side
    manifest = process(args.input, args.output_dir, max_long_side=max_long_side, roi=args.roi)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
