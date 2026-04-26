# 教程五：RTI之后的前沿技术

## 学习目标

理解为什么传统RTI还不够，以及哪些新技术可以更好地实现“微痕扫描、数字拓片、线图生成、全信息模型和AI识读”。

## 先记住一句话

传统RTI擅长“看见浅表面细节”，但不一定擅长“定量测量、复杂材质、高可信线图和自动识读”。前沿路线就是补这些短板。

## 推荐学习顺序

### 1. 校准光度立体

先读：
- `../papers/18_DiLiGenT_Pi_Photometric_Stereo_Near_Planar_Rich_Details_ICCV2023.pdf`
- `../papers/09_Photometric_Stereo_3D_Reconstruction_Artworks.pdf`

要理解：
- 为什么“近似平面 + 丰富细节”正好对应碑刻、甲骨、汉画像石。
- 法线图和高度图比传统RTI增强图多了什么。
- 光源标定为什么比手持H-RTI更可靠。

实践任务：
- 设计8个方向光源：N、S、E、W和四个对角。
- 采集硬币或刻字石片。
- 输出法线图和虚拟掠射光图。

### 2. MLIC和BRDF/法线优化

先读：
- `../papers/19_BRDF_Monotonicity_Shading_Normals_MLIC_GCH2024.pdf`

要理解：
- MLIC就是多光照图像集合，是传统RTI、光度立体、BRDF估计的共同数据底座。
- 几何法线和视觉重打光用的shading normal可以分开。
- 微痕结果要可信，不能只靠“看起来更锐”。

实践任务：
- 以后每组采集都保存原始MLIC，不只保存RTI输出。
- 对每个输出标记来源：PTM、RBF、法线图、增强算法、人工修正。

### 3. 多光谱/高光谱RTI

先读：
- `../papers/22_Multispectral_RTI_Integrated_Angular_Spectral_Reflectance.pdf`

要理解：
- RTI主要看几何纹理，多光谱看材料和波段差异。
- 对有颜料、污染、墨迹、风化层的对象，多光谱很有价值。
- 对纯石刻，价值可能不如光度立体直接，但能辅助区分材料噪声。

实践任务：
- 先尝试可见光和近红外两组照片。
- 比较红外下刻痕、污染和石材纹理是否分离得更好。

### 4. 偏振成像

先读：
- `../papers/20_Shape_From_Polarization_Cultural_Heritage_2024.pdf`
- `../papers/21_Polarization_UNet_Surface_Normal_2024.pdf`

要理解：
- 偏振信息能帮助估计表面法线。
- 对高反光、低纹理、摄影测量困难的表面有意义。
- 普通相机加旋转偏振片可以做入门实验。

实践任务：
- 同一对象拍0、45、90、135度偏振图。
- 比较普通照片、RTI照片、偏振照片对微痕的表现。

### 5. Neural RTI

先读：
- [DisK-NeuralRTI](https://iris.univr.it/handle/11562/1162371)
- [Efficient neural relightable images for cultural heritage](https://iris.cnr.it/handle/20.500.14243/532852)

要理解：
- Neural RTI用神经网络替代PTM/HSH固定函数。
- 复杂反射和高光表现更强。
- 但部署复杂、可解释性弱，不适合作为第一版。

实践任务：
- 暂不实现。
- 保留高质量MLIC数据，为以后训练神经模型准备。

### 6. AI线图和数字拓片

先读：
- [Relic2Contour](https://www.nature.com/articles/s40494-025-01606-0)
- [Point cloud line drawings](https://www.nature.com/articles/s40494-025-01678-y)
- [Archaeological line drawings from limited references](https://www.nature.com/articles/s40494-026-02526-3)

要理解：
- 汉画像石研究最终需要线图、拓片、标注，不只是增强图。
- AI可以辅助，但必须保留人工复核。
- 我们应先建立小规模“增强图 -> 人工线图”的数据集。

实践任务：
- 用OpenCV做第一版线图。
- 让人工修正。
- 保存成训练数据。

## 我们的近期路线

第一优先级不是Neural RTI，而是：

```text
固定光源矩阵
  → 校准光度立体
  → 法线图/虚拟掠射光
  → 数字拓片
  → 线图
  → 全信息模型
```

原因：
- 直接服务微痕。
- 硬件可控。
- 算法可解释。
- 能与公开资料中的“光源矩阵、微痕增强、电子拓片、线图”路线对应。

## 本课输出

读完后写一页总结：

- 哪三项技术最适合近期复现？
- 哪三项技术适合后续研究储备？
- 对汉画像石来说，RTI、光度立体、3D扫描、多光谱、AI线图分别负责什么？
