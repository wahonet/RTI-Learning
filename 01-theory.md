# 01 RTI理论基础

## 学习目标

建立RTI（Reflectance Transformation Imaging）的基础知识框架，理解它如何通过固定相机、多角度光照和每像素反射建模，把浅浮雕、刻痕、纹理和风化表面的细节变成可交互重打光的数据。

本阶段先不讨论具体汉画像石应用，也不急于复现微痕成像工程路线。重点是掌握RTI本身的数学、采集、格式和可视化基础。

## 核心概念

- RTI：反射变换成像，通过多张不同光照方向下的照片，拟合每个像素对光照方向的响应。
- PTM：Polynomial Texture Mapping，早期RTI代表方法，用二次多项式表示每个像素亮度随光照方向的变化。
- HSH：Hemispherical Harmonics，用半球谐函数表示半球光照下的反射变化。
- RBF：Radial Basis Function，现代RTI工具中常见的插值/拟合方式，Relight常用。
- 光度立体：Photometric Stereo，从多光照图像估计表面法线，有时可进一步积分得到高度图。
- 法线图：用RGB颜色编码每个像素表面方向，适合观察微小凹凸。
- 增强渲染：通过虚拟光照、漫反射增益、镜面增强、法线增强等方式突出表面细节。

## 经典理论资料

### Cultural Heritage Imaging RTI Capture

链接：[Cultural Heritage Imaging: RTI Capture](https://culturalheritageimaging.org/What_We_Offer/Downloads/Capture/)

用途：
- 学习固定相机、多角度光源、反光球和采集顺序。
- 理解水平采集、垂直采集和野外采集的差异。
- 建立后续采集SOP的基础。

重点问题：
- 为什么相机和对象必须保持固定？
- 光源方向为什么要覆盖半球？
- 反光球如何用于估计光照方向？
- 环境光、曝光和阴影会怎样影响拟合？

### Cultural Heritage Imaging Processing Guide

链接：[Cultural Heritage Imaging: RTIBuilder / Processing](https://culturalheritageimaging.org/What_We_Offer/Downloads/Process/)

用途：
- 学习传统RTIBuilder处理流程。
- 理解图像预处理、光照检测、拟合和输出文件之间的关系。
- 了解PTM和HSH输出的历史工具链。

重点问题：
- RTIBuilder如何从高光球推算光照方向？
- PTM和HSH各自适合什么表面？
- 为什么RTIBuilder现在更适合作为参考流程，而不是长期主工具？

### Polynomial Texture Maps

链接：[Polynomial Texture Maps, Malzbender et al. 2001](https://www.readkong.com/page/polynomial-texture-maps-tom-malzbender-dan-gelb-hans-8576098)

用途：
- 掌握PTM的原始理论。
- 理解每像素多项式拟合和交互重打光。
- 理解RTI为什么适合楔形文字、硬币、浅浮雕、碑刻和微痕。

核心公式方向：
- 每个像素的亮度由光照方向投影决定。
- 典型LRGB PTM使用6个多项式系数拟合亮度变化。
- 颜色信息和亮度响应可以分开存储。

需要摘录的问题：
- PTM对Lambertian和非Lambertian表面的假设是什么？
- 二次多项式能捕捉哪些细节，不能捕捉哪些细节？
- 对于粗糙石材，拟合误差可能来自哪里？

### Library of Congress PTM Format

链接：[Library of Congress: PTM Format Description](https://www.loc.gov/preservation/digital/formats/fdd/fdd000487.shtml)

用途：
- 学习PTM/RTI作为数字保存格式的优缺点。
- 理解长期保存、格式开放性和可读性的关系。
- 为后续数据结构设计提供参考。

重点问题：
- PTM和RTI文件如何记录系数？
- 这类文件适合作为最终档案，还是适合作为处理结果？
- 原始照片序列是否必须长期保存？

## 理论学习笔记模板

每读一篇论文或指南，按下面格式补充：

```markdown
## 资料标题

- 链接：
- 类型：论文 / 指南 / 工具文档 / 案例
- 关键词：
- 核心问题：
- 方法摘要：
- 对汉画像石/碑刻的启发：
- 后续实验：
```

## 需要掌握的技术问题

### 图像采集

- 相机必须固定，避免像素位置变化导致拟合失败。
- 所有照片应尽量保持同一曝光、焦距、白平衡和光圈。
- 光照方向要覆盖上半球，低角度掠射光对刻痕特别重要。
- 反光球、高光点或固定光源几何都可用于光向估计。

### 光照建模

- 手持高光法：光源自由移动，通过反光球恢复光向。
- 固定光源法：光源位置已知，适合LED矩阵和半球装置。
- 光源强度需要尽量一致，或在处理阶段做归一化。
- 光源过近时不能简单视为平行光，需要考虑近场照明。

### 表面建模

- PTM/HSH/RBF偏重可交互重打光。
- 光度立体偏重法线图和高度图估计。
- RTI不等于真正三维扫描，但能提供2.5D表面线索。
- 对汉画像石这类浅浮雕，RTI可与三维扫描互补。

### 增强显示

- 交互重打光：人工寻找最能显示刻痕的光照角度。
- Diffuse gain：增强局部漫反射变化。
- Specular enhancement：突出微小表面方向变化。
- Normal visualization：用伪彩色查看表面方向。
- Synthetic grazing light：合成低角度掠射光，适合碑文和线刻。

## 本阶段交付物

- RTI术语表初稿。
- PTM/HSH/RBF/光度立体方法对比表。
- 每种增强模式的视觉效果说明。
- 至少5篇核心资料的摘要。

## 待办

- [ ] 阅读CHI RTI Capture Guide。
- [ ] 阅读CHI Processing Guide。
- [ ] 阅读Malzbender 2001 PTM论文。
- [ ] 整理PTM核心公式和变量解释。
- [ ] 整理RTI文件格式和原始照片保存策略。
