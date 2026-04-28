# 样例输出说明

输入图：`inputs/image2_b842e.png`

运行命令：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
```

看图顺序：

1. `contact_sheet.jpg`：总览，先判断哪种视图对肉眼读字最有帮助。
2. `04_illumination_flattened.png`：看大面积光照和阴影是否被压平。
3. `07_directional_gabor_strokes.png`：看竖、横、斜细笔画是否浮出来。
4. `08_morphological_stroke_energy.png`：看可能的笔画能量位置，但它也会突出划痕。
5. `09_relief_light_ne.png` / `10_relief_light_sw.png`：模拟不同侧光，适合放大看浅刻凹凸。
6. `11_adaptive_binary_candidate.png`：只是 OCR 候选输入，不是可靠释文。

目前这张图的主要问题是表面划痕和反光与字形非常相似。传统增强可以辅助观察，但要想稳定 OCR，建议重新拍多方向侧光或 RTI。
