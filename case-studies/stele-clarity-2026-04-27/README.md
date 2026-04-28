# 碑刻文字清晰化与 AI 识读资料包

这个文件夹把“怎么把照片上的碑刻字看清、识别、结构化”分成四件事：

1. `01_research_map.md`：论文、GitHub 仓库、数据集和研究方向总览。
2. `02_practical_pipeline.md`：针对你这几张照片的建议流程，从重新拍照到 OCR/校读。
3. `03_acquisition_research.md`：石刻、碑刻、画像石精细采集的论文、项目、仓库和设备路线。
4. `04_learning_route_for_humanities.md`：文科背景学习路线、教程、参考书和 6 个月计划。
5. `05_han_pictorial_stone_structuring.md`：汉画像石图像结构化的研究领域、数据模型和落地路线。
6. `06_yolo_learning_route.md`：YOLO 入门解释，以及面向汉画像石检测/结构化的学习路线。
7. `sources.csv` / `acquisition_sources.csv` / `han_pictorial_stone_structuring_sources.csv`：可点开的来源索引，方便继续阅读。
8. `tools/stele_enhance.py`：一个先跑起来的 OpenCV 样例脚本。

合并到 `RTI-Learning` 后，三张原图和实验输出默认不纳入 Git 跟踪；它们仍保留在本地旧目录 `E:\relics-align2\stele_clarity_research_2026-04-27`。如需复现实验，把图片复制到本目录的 `inputs/`，或把命令里的图片路径改成本地旧目录中的原图路径。

快速复现实验：

```powershell
cd E:\relics-align2\stele_clarity_research_2026-04-27
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
```

对局部文字区域做放大实验：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e_crop --roi 850 100 3000 1900
```

脚本会输出多种视图：去红色坐标叠字、光照校正、局部对比、方向滤波、伪侧光、形态学笔画能量图、二值化候选图和总览拼图。最值得先看的通常是 `contact_sheet.jpg`、`07_directional_gabor_strokes.png`、`08_morphological_stroke_energy.png`、`09_relief_light_ne.png`、`10_relief_light_sw.png`。

重要判断：单张普通照片只能改善“可见性”，不能可靠恢复已经没有成像信息的笔画。若目标是可被计算机识别并结构化，最优路线是重新采集多光照/RTI 或三维表面信息，再用训练过的碑刻/拓片增强模型与 OCR/大模型校读串起来。
