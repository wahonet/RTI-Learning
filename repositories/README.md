# GitHub仓库与工具源码索引

本目录用于保存与RTI/PTM、光度立体、神经重光照、文物线图、考古标注和AI检测相关的开源仓库快照或复现入口。

总索引见：

- `../research-master-index-2026.csv`
- `../learning-roadmap.html`

## 本地已下载

### `github/NeuralRTI`

来源：[Univr-RTI/NeuralRTI](https://github.com/Univr-RTI/NeuralRTI)

用途：Keras版NeuralRTI，实现像素级RTI编码和神经重光照。它是研究神经RTI、DisK-NeuralRTI和OpenLIME神经可重光照展示的基础代码。

说明文档：`github/NeuralRTI_NOTE.md`

## 网络受限，暂未完整下载

以下仓库在本机通过代理下载时出现长时间无响应或中断，先记录复现入口，后续可在网络稳定时补充源码快照。

### `cnr-isti-vclab/relight`

链接：[https://github.com/cnr-isti-vclab/relight](https://github.com/cnr-isti-vclab/relight)

用途：RelightLab/Relight CLI，当前最重要的现代RTI/PTM/HSH/RBF处理工具之一，支持法线图、Web格式、OpenLIME生态。

### `cnr-isti-vclab/openlime`

链接：[https://github.com/cnr-isti-vclab/openlime](https://github.com/cnr-isti-vclab/openlime)

用途：Web端多层图像浏览器，支持RTI、多光谱、BRDF、IIIF、DeepZoom和标注扩展，是后续发布RTI和IIML标注的重点方向。

### `NU-ACCESS/ImageJ-Photometric-Stereo-tools`

链接：[https://github.com/NU-ACCESS/ImageJ-Photometric-Stereo-tools](https://github.com/NU-ACCESS/ImageJ-Photometric-Stereo-tools)

用途：ImageJ/Fiji环境中的光度立体工具，用RTI式掠射光图像估计法线和高度，适合文物表面微起伏实验。

### `visiont3lab/photometric_stereo`

链接：[https://github.com/visiont3lab/photometric_stereo](https://github.com/visiont3lab/photometric_stereo)

用途：Python/OpenCV实现Woodham光度立体，适合作为教学和小样本基线。

### `yqueau/near_ps`

链接：[https://github.com/yqueau/near_ps](https://github.com/yqueau/near_ps)

用途：近场点光源光度立体Matlab代码，适合LED灯阵和近距离文物采集。

### `laclark/cuneiform_lineart`

链接：[https://github.com/laclark/cuneiform_lineart](https://github.com/laclark/cuneiform_lineart)

用途：楔形文字线图生成相关代码，对浅刻文字和汉画像石线图有方法参考价值。

### `lrncrd/Ceramatic2.0`

链接：[https://github.com/lrncrd/Ceramatic2.0](https://github.com/lrncrd/Ceramatic2.0)

用途：考古陶器自动绘图工具，包含YOLO模型和考古出版图输出流程，可借鉴“AI检测 -> 标准化线图”的工程组织方式。

### `akhawaja2014/Beyond-Relighting`

链接：[https://github.com/akhawaja2014/Beyond-Relighting](https://github.com/akhawaja2014/Beyond-Relighting)

用途：2026年RTI + 深度学习聚类纺织品碎片论文的代码仓库。对本项目“RTI不只是可视化，也可作为AI特征输入”很重要。

### `BeebBenjamin/RTIPy`

链接：[https://github.com/BeebBenjamin/RTIPy](https://github.com/BeebBenjamin/RTIPy)

用途：Python + Arduino便携微型RTI dome方案，含3D打印、LED控制和相机触发思路。适合低成本硬件设计参考。

### `leszekmp/artid`

链接：[https://github.com/leszekmp/artid](https://github.com/leszekmp/artid)

用途：Affordable Reflectance Transformation Imaging Dome，约600美元级别自动RTI dome方案，适合学习硬件结构和控制流程。

### `nichlock/rti`

链接：[https://github.com/nichlock/rti](https://github.com/nichlock/rti)

用途：开源RTI硬件和软件实现，包含Arduino Mega shield、三色LED矩阵和GUI控制界面。

### `cvat-ai/cvat`

链接：[https://github.com/cvat-ai/cvat](https://github.com/cvat-ai/cvat)

用途：工业级图像/视频标注平台，支持YOLO、COCO、Ultralytics格式、分割和SAM自动标注。适合正式汉画像石标注项目。

### `HumanSignal/label-studio`

链接：[https://github.com/HumanSignal/label-studio](https://github.com/HumanSignal/label-studio)

用途：多类型数据标注平台，适合把图像标注、文本、研究说明和模型预标注接入统一流程。

### `vietanhdev/anylabeling`

链接：[https://github.com/vietanhdev/anylabeling](https://github.com/vietanhdev/anylabeling)

用途：本地AI辅助标注工具，支持YOLOv8、SAM、SAM2、SAM2.1、SAM3和MobileSAM。适合个人快速制作YOLO/SAM小数据集。

### `recogito/annotorious`

链接：[https://github.com/recogito/annotorious](https://github.com/recogito/annotorious)

用途：Web图像标注组件，支持IIIF/OpenSeadragon生态，可作为后续IIML标注前端的参考。

### `colmap/colmap`

链接：[https://github.com/colmap/colmap](https://github.com/colmap/colmap)

用途：Structure-from-Motion和Multi-View Stereo工具，用于整体三维模型、相机位姿估计、正射图生成和局部RTI配准。

### `alicevision/meshroom`

链接：[https://github.com/alicevision/meshroom](https://github.com/alicevision/meshroom)

用途：开源节点式摄影测量和三维重建框架。适合非代码方式搭建3D重建流程，也可评估Photometric Stereo节点。

### `CloudCompare/CloudCompare`

链接：[https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare)

用途：点云和网格质检、裁剪、配准、距离分析。适合比较RTI/光度立体结果与3D扫描结果。

### `potree/potree`

链接：[https://github.com/potree/potree](https://github.com/potree/potree)

用途：WebGL大型点云浏览器，用于公开展示或内部浏览汉画像石点云数据。

### `IIIF/mirador`

链接：[https://github.com/IIIF/mirador](https://github.com/IIIF/mirador)

用途：IIIF多图像比较查看器，适合比较原图、拓片、RTI增强图、线图和不同馆藏图像。

### `UniversalViewer/universalviewer`

链接：[https://github.com/UniversalViewer/universalviewer](https://github.com/UniversalViewer/universalviewer)

用途：IIIF和多媒体查看器，可展示图像、3D、PDF、音视频，适合未来研究包发布评估。

### `ultralytics/ultralytics`

链接：[https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

用途：YOLO训练、推理和SAM自动标注入口。其`auto_annotate`流程可用YOLO检测框驱动SAM生成分割标签。

### `dataversioncontrol/dvc`

链接：[https://github.com/dataversioncontrol/dvc](https://github.com/dataversioncontrol/dvc)

用途：大数据、训练集、模型和实验输出版本管理。适合解决RAW图像和模型权重不进Git但仍可追溯的问题。
