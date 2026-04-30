# NeuralRTI, Neural Reflectance Fields, and DisK-NeuralRTI

相关资料：

- [Neural reflectance transformation imaging, 2020](https://link.springer.com/article/10.1007/s00371-020-01910-9)
- [Univr-RTI/NeuralRTI](https://github.com/Univr-RTI/NeuralRTI)
- [DisK-NeuralRTI, 2024](https://tgdulecha.github.io/Disk-NeuralRTI/)
- [Fast and accurate neural reflectance transformation imaging through knowledge distillation, 2025](https://arxiv.org/html/2510.24486v1)
- [A Neural Reflectance Field Model for Accurate Relighting in RTI Applications, 2025](https://iris.unive.it/handle/10278/5103913)

本地仓库快照：`repositories/github/NeuralRTI`

## NeuralRTI 2020

NeuralRTI用自编码器学习RTI数据的像素级编码和重光照函数。传统PTM/HSH使用固定基函数拟合光照方向到像素颜色的关系，在高光、阴影和复杂材质上容易出现伪影。NeuralRTI把每个像素的多光照观测压缩为低维编码，再用decoder根据编码和新光照方向预测RGB值。

本地源码显示其实现基于Keras：

- `train.py`读取`dirs.lp`光照方向和图像序列。
- `relighting_model.py`定义encoder-decoder结构。
- encoder把每个像素的多光照观测压缩为`compcoeff`维编码。
- decoder输入像素编码和二维光照方向，输出RGB。

## DisK-NeuralRTI 2024/2025

NeuralRTI质量较高，但decoder网络比PTM/HSH慢，尤其大图和Web浏览时性能不足。DisK-NeuralRTI使用知识蒸馏，把原始teacher decoder压缩为小student decoder。文献称可减少约80%参数，并在在线查看器中接近10倍加速，使神经RTI更接近实际文博部署。

## Neural Reflectance Field RTI 2025

2025年的Neural Reflectance Field Model进一步把RTI表面反射描述为隐式神经表示。输入包括像素坐标、光照方向和局部邻域反射潜变量。它试图比单纯像素自编码更好地表达局部表面和复杂阴影。

## 对汉画像石的价值

神经RTI不是第一阶段必需，但非常适合作为“更好、更现代、更吸引人”的前沿方向：

- 粗糙石材、阴影、裂隙和高光可能比PTM/HSH更难拟合，神经模型可能提高重光照质量。
- 可把原始MLIC保存下来，未来训练NeuralRTI，不被传统格式锁死。
- Web端展示可关注OpenLIME对神经可重光照图像的支持。

## 风险

- 可解释性弱于PTM、HSH和光度立体。
- 训练成本和部署复杂度高。
- 对考古释读而言，生成效果更好不等于更真实，必须保留原始多光照图像和传统拟合结果作为对照。

## 项目策略

第一阶段不训练神经RTI，只做三件事：

- MLIC原始数据规范化保存。
- 用Relight/PTM/HSH/RBF和光度立体建立传统基线。
- 保留NeuralRTI实验目录和小样本复现计划。

第二阶段再尝试：

- 复现本地`NeuralRTI`示例数据。
- 比较PTM/HSH/RBF/NeuralRTI在石刻样本上的重光照误差。
- 调研DisK-NeuralRTI是否有公开代码或OpenLIME插件。
