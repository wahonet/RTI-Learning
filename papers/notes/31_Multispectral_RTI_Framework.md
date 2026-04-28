# Extended Framework for Multispectral RTI

来源：[HAL开放文本](https://hal.science/hal-03836363/document)

PDF状态：本机下载直链返回不可读小文件；仓库已有早期PDF `papers/22_Multispectral_RTI_Integrated_Angular_Spectral_Reflectance.pdf`，本笔记作为补充阅读记录。

## 论文在做什么

这项研究把多光照RTI和多光谱成像结合，形成Multispectral RTI。传统RTI记录角度反射，MSI记录不同波段下的材料/颜色差异。MS-RTI希望同时在光照方向和光谱波段两个维度上探索文物表面。

## 方法

使用自建dome系统，包含12.4MP单色相机和多个波长光源：

- 365 nm。
- 395 nm。
- 505 nm。
- 530 nm。
- 625 nm。
- 850 nm。

作者提出用图像样条插值重建角度和光谱反射，并开发了用于Multispectral-RTI探索的可视化工具。案例包括纸本水粉画和20世纪锡盒。

## 对汉画像石的价值

汉画像石主要看表面几何，但仍可能存在：

- 颜料残留。
- 拓印墨迹。
- 污染层。
- 石材矿物差异。
- 修复痕迹。

MS-RTI可以同时区分“形态线索”和“材料线索”。例如同一条暗线可能是刻痕、裂隙、墨迹或污染，光谱维度能辅助判断。

## 近期可做低成本版本

不必一开始建设完整多光谱dome，可先做：

- 可见光RTI。
- 近红外灯或改机相机的小样本对照。
- UV诱导可见荧光照片。
- 同一局部多波段图像配准。

## 局限

- 完整MS-RTI硬件复杂，成本和标定要求高。
- 光谱维度增加后数据量显著变大。
- 对纯石刻线条的收益需要实验验证。

## 后续任务

- 为采集SOP增加“可选多波段扩展”。
- 对有拓印墨迹或颜料残留的样本优先测试NIR/UV。
- 在IIML资源层加入`spectralBand`和`illuminationDirection`字段。
