# 碑刻照片清晰化案例

这个案例的起点很简单：几张碑刻照片上的字太浅，用灰度、锐化、对比度这些办法处理后，基本没有多认出字，也不适合直接 OCR。

后面整理的结论是：这不是单张照片后期能解决的问题。要想读字，应该回到采集阶段，用多方向斜光、RTI、光度立体或三维扫描把碑面的凹凸信息采下来。

## 这个目录里有什么

- [01_research_map.md](01_research_map.md)：碑刻文字清晰化、识别和结构化资料。
- [02_practical_pipeline.md](02_practical_pipeline.md)：针对这批照片的实际处理和重新采集建议。
- [03_acquisition_research.md](03_acquisition_research.md)：石刻、碑刻、画像石精细采集资料。
- [04_learning_route_for_humanities.md](04_learning_route_for_humanities.md)：文科背景学习路线。
- [05_han_pictorial_stone_structuring.md](05_han_pictorial_stone_structuring.md)：汉画像石图像结构化。
- [06_yolo_learning_route.md](06_yolo_learning_route.md)：YOLO 是什么，以及怎么学。
- [tools/stele_enhance.py](tools/stele_enhance.py)：之前试过的 OpenCV 增强脚本，保留作失败经验和基线。

## 我现在的判断

单张普通照片后期只能改善“看起来清楚一点”，但不能凭空恢复没拍到的笔画。对于风化浅刻碑文，更值得投入的是：

1. 现场重新拍多方向斜光。
2. 尝试 RTI，让电脑里可以反复换光方向。
3. 对重点文物做摄影测量、结构光或激光扫描。
4. 从 3D 数据里生成数字拓片、曲率图、法线图。
5. 最后再谈 OCR、YOLO、知识图谱和 AI 校读。

## 本地数据

原始图片和输出图没有放进 GitHub。它们带经纬度水印，而且文件较大。当前仓库只保留文档、来源索引和脚本。

如果要复现实验，可以把本地图片复制到 `inputs/`，再运行：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
```

局部裁剪实验：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e_crop --roi 850 100 3000 1900
```

这个脚本不是最终方案，只是说明传统图像增强的上限在哪里。
