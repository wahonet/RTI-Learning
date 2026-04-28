# NeuralRTI 仓库阅读笔记

本地源码：`repositories/github/NeuralRTI`

上游仓库：[https://github.com/Univr-RTI/NeuralRTI](https://github.com/Univr-RTI/NeuralRTI)

许可证：MIT

## 仓库做什么

这是论文 *Neural reflectance transformation imaging* 的Keras实现。它把传统RTI中的“多光照像素观测 -> 任意光照下像素颜色”建模为神经网络，而不是PTM/HSH这类固定基函数。

## 输入数据格式

README要求数据目录包含：

- 多张同视角、不同光照方向图像。
- `dirs.lp`光照方向文件。

训练命令：

```bash
python train.py --data_path exampledataset
```

测试/重光照命令：

```bash
python test.py --model_files exampledataset/model_files --light_dir exampledataset/test_lightdirs
```

## 代码结构

- `train.py`：读取光照方向和图像序列，训练encoder-decoder，保存像素编码、header、decoder模型和TensorFlow.js格式。
- `test.py`：读取训练得到的模型文件和测试光照方向，输出重光照结果。
- `relighting_model.py`：定义核心神经网络。
- `computeaph.py`：把图像序列整理成训练用像素观测和光照方向。

`relighting_model.py`中的模型分为：

- encoder：把每个像素的多光照观测压缩成低维编码。
- decoder：输入像素编码和光照方向，输出RGB。
- autoencoder：训练时端到端拟合原始多光照观测。

## 对RTI/PTM的意义

传统RTI文件通常保存每个像素的一组多项式或HSH系数。NeuralRTI保存的是：

- 每个像素的低维神经编码。
- 一个共享decoder网络。

这种方式可能更好处理高光、阴影、复杂材质和非线性反射，但渲染速度和部署复杂度高于PTM/HSH。

## 对汉画像石的适配价值

汉画像石表面可能包含石材颗粒、裂缝、风化凹凸、拓印墨迹和低浮雕边界。神经RTI可作为高阶实验，用来比较：

- PTM/HSH/RBF传统拟合。
- RelightLab输出。
- 光度立体法线图。
- NeuralRTI重光照质量。

## 复现建议

第一步只跑仓库自带`exampledataset`，确认Python/Keras/TensorFlow版本。该仓库较老，README测试环境是Python 3.5、Keras 2.3.1、TensorFlow 2.1，现代环境可能需要单独Docker或conda环境。

第二步使用自采硬币或刻痕板MLIC测试。暂不直接用于正式汉画像石释读，必须和原始图像及传统RTI输出对照。

## 风险

- 代码年代较早，依赖可能难安装。
- 神经输出可能更“好看”，但解释性弱。
- 若用于研究发表，需要明确它是重光照模型，不是几何真值。
