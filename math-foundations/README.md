# RTI/光度立体/AI线图所需数学基础

本目录用于把论文中的数学概念拆成中文学习路线。目标不是系统考研高数，而是让你能看懂 RTI、PTM、HSH、光度立体、法线图、优化、神经网络和线图生成论文里真正会用到的数学。

中文 HTML 小课入口：

- `html/index.html`

## 本地教材

PDF 放在 `downloads/`，该目录默认不进 Git。已经下载的开放资料包括：

- `downloads/openstax-calculus-volume-1.pdf`
- `downloads/openstax-calculus-volume-2.pdf`
- `downloads/openstax-calculus-volume-3.pdf`
- `downloads/boyd-vandenberghe-introduction-to-applied-linear-algebra.pdf`
- `downloads/boyd-vandenberghe-convex-optimization.pdf`
- `downloads/mathematics-for-machine-learning.pdf`

## 为什么这些数学和 RTI 有关

### 1. 函数、导数、梯度

RTI、PTM 和神经网络都在处理“输入改变，输出怎么改变”。例如：

```text
光照方向改变 -> 像素亮度改变
参数改变 -> 误差改变
表面高度改变 -> 法线方向改变
```

导数描述变化率，梯度描述多变量情况下“往哪里变最快”。论文里出现 optimization、gradient descent、normal integration 时，都离不开这部分。

### 2. 向量和矩阵

光照方向、表面法线、相机方向都可以写成向量。多张照片、多盏灯、多像素组成矩阵。光度立体最核心的关系常被写成：

```text
I = L n
```

可以读成：观测亮度 `I` 由光照矩阵 `L` 和表面法线 `n` 决定。要求 `n`，就会进入线性代数和最小二乘。

### 3. 最小二乘

真实照片有噪声，光照也不完美。算法通常不是找到完全满足公式的答案，而是找一个“误差总和最小”的答案。这就是最小二乘。

它在以下论文概念中反复出现：

- PTM 系数拟合。
- 光度立体法线估计。
- 相机/灯位标定。
- 神经网络训练中的损失最小化。

### 4. 多元函数和偏导

PTM 用光照方向参数 `(u, v)` 预测像素亮度。高度图是二维平面上的函数：

```text
z = h(x, y)
```

偏导数 `∂h/∂x` 和 `∂h/∂y` 描述表面朝 x/y 方向的倾斜程度，和法线图、数字拓片、虚拟斜光直接相关。

### 5. 优化

BRDF 拟合、法线优化、神经 RTI、扩散模型线图都要解优化问题。最简单地说：

```text
先定义误差
再调整参数
让误差越来越小
```

高阶论文里的 loss、regularization、constraint、convex、non-convex 都属于优化语言。

## 针对论文的数学阅读顺序

1. H-RTI 采集类论文：先懂几何直觉，不需要高数。
2. PTM/HSH/RBF：学习函数、二次多项式、最小二乘。
3. 光度立体：学习向量、矩阵、法线、最小二乘。
4. 法线积分/高度图：学习偏导、梯度、积分和泊松方程的直觉。
5. BRDF/反射模型：学习向量夹角、点积、半角向量和优化。
6. Neural RTI/AI线图：学习矩阵、梯度下降、损失函数、卷积/Transformer 的基本概念。

## 当前最该先学的章节

如果只服务 RTI 和光度立体，优先级是：

1. OpenStax Calculus Volume 1：极限、导数、积分的直觉。
2. OpenStax Calculus Volume 3：向量、偏导、梯度、多元函数。
3. VMLS：向量、矩阵、最小二乘。
4. Mathematics for Machine Learning：矩阵分解、优化和概率。
5. Convex Optimization：只读 least-squares、gradient、convex sets 的入门部分即可。

## 中文 HTML 小课

- `html/01-vectors-light-normals.html`：光照方向和表面法线为什么是向量。
- `html/02-dot-product-raking-light.html`：点积如何解释斜光明暗。
- `html/03-least-squares-fitting.html`：PTM 系数为什么用最小二乘拟合。
- `html/04-matrices-photometric-stereo.html`：从多张照片求法线图。
- `html/05-gradient-normal-height.html`：高度图、梯度和法线积分。
- `html/06-loss-optimization-ai.html`：神经 RTI 里的损失函数和梯度下降。
- `html/07-calculus-roadmap.html`：高数入门路线。
- `html/08-reading-formulas.html`：英文论文公式阅读方法。
