# Reflectance Transformation Imaging for Detecting Knots in Heritage Timbers

本地PDF：`papers/reading/02-heritage-epigraphy-cases/23-RTI_Heritage_Timbers/23-RTI_Heritage_Timbers.pdf`

来源：[ISPRS Archives, 2025](https://isprs-archives.copernicus.org/articles/XLVIII-M-9-2025/1289/2025/)

## 论文在做什么

论文把RTI用于历史木构件节疤检测。节疤会影响木材强度和等级判断，但历史木构表面常有灰尘、油漆和颜色变化，普通照片下不易识别。作者制作了低成本手持RTI dome，用不同光照方向采集木梁局部，再用RTI模型辅助检测节疤。

## 方法

论文的核心是“RTI + SfM”：

- 用手持低成本RTI dome采集同一局部多光照图像。
- 通过RTI重打光观察节疤在不同光照下的可见性。
- 把RTI图像子集送入Structure from Motion，生成3D模型。
- 比较不同图像子集对三维重建质量和计算时间的影响。
- 与普通DSLR相机摄影测量模型对比颜色和几何。

论文还提到项目中有基于预训练YOLOv8m的木节疤AI检测管线。

## 对汉画像石的价值

这篇论文虽然对象是木构，但对汉画像石现场采集非常有启发：

- 手持低成本RTI dome适合不可移动、现场空间受限的对象。
- RTI图像不只用于重打光，也可复用到SfM，减少重复采集。
- 可以把RTI局部模型投到整体3D模型上，解决局部信息定位问题。
- YOLO检测可以在RTI增强图或SfM正射图上运行，用于候选区域发现。

## 可迁移到本项目的流程

```text
整体对象普通摄影测量
  -> 获得画像石整体坐标和正射图
  -> 对关键局部使用手持RTI dome或固定灯阵
  -> 生成RTI/法线图/增强图
  -> 把局部RTI区域登记回整体模型或IIIF图像
  -> 在增强图上做YOLO/SAM/IIML标注
```

## 局限

- 木材节疤和石刻线条的反射/纹理机制不同。
- 论文关注检测节疤，不涉及图像学语义。
- 手持dome对大幅画像石可能需要分区、拼接和配准。

## 后续任务

- 设计便携RTI dome或半圆灯架。
- 测试RTI图像是否能直接用于本项目SfM流程。
- 建立“局部RTI采集区域 -> 整体对象坐标”的元数据字段。
