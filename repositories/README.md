# GitHub仓库与工具源码索引

本目录用于保存与RTI/PTM、光度立体、神经重光照、文物线图、考古标注和AI检测相关的开源仓库快照或复现入口。

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
