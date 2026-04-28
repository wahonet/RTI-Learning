# 碑刻照片清晰化案例

本案例来自几张难以识读的碑刻照片。灰度、锐化、对比度增强等后期处理没有明显增加可识读文字，也不适合作为 OCR 输入。

结论是：问题主要出在采集阶段。浅刻、风化和低对比碑文需要通过多方向斜光、RTI、光度立体或三维扫描记录表面凹凸信息，单张普通照片后期处理的提升有限。

## 目录内容

- [01_research_map.md](01_research_map.md)：碑刻文字清晰化、识别和结构化资料。
- [02_practical_pipeline.md](02_practical_pipeline.md)：单张照片处理和重新采集建议。
- [03_acquisition_research.md](03_acquisition_research.md)：石刻、碑刻、画像石精细采集资料。
- [04_learning_route_for_humanities.md](04_learning_route_for_humanities.md)：文科背景学习路线。
- [05_han_pictorial_stone_structuring.md](05_han_pictorial_stone_structuring.md)：汉画像石图像结构化。
- [06_yolo_learning_route.md](06_yolo_learning_route.md)：YOLO 目标检测学习路线。
- [tools/stele_enhance.py](tools/stele_enhance.py)：OpenCV 增强脚本，作为传统图像增强基线保留。

## 技术判断

普通照片后期只能改善局部可见性，不能恢复采集时没有记录下来的笔画信息。风化浅刻碑文更适合以下流程：

1. 现场重新拍摄多方向斜光。
2. 使用 RTI 记录同一表面在不同光照下的变化。
3. 对重点文物使用摄影测量、结构光或激光扫描。
4. 从三维数据中生成数字拓片、曲率图和法线图。
5. 在采集质量稳定后，再进行 OCR、YOLO、知识图谱和 AI 校读。

## 本地数据

原始图片和输出图没有放进 GitHub。原因是原图带经纬度水印，文件体积较大。当前仓库只保留文档、来源索引和脚本。

复现实验时，可将本地图片复制到 `inputs/`，然后运行：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
```

局部裁剪实验：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e_crop --roi 850 100 3000 1900
```

该脚本不是最终方案，主要用于说明传统图像增强的上限。
