# 08 前沿技术路线：超越传统RTI

## 背景

传统RTI/PTM/H-RTI在2000年前后形成，优势是低成本、可交互重打光、适合浅刻和微痕观察。但它也有明显限制：

- PTM/HSH使用固定基函数，复杂反射、阴影、强高光和粗糙石材会产生伪影。
- H-RTI的手持光源和反光球估计不够定量。
- RTI通常偏“视觉增强”，不直接提供可靠三维高度。
- 传统RTI输出对AI识读、数字拓片、线图生成支持不足。

因此，后续不宜只复刻2000年代RTI，而应把RTI作为基础，叠加近年的多光照成像、光度立体、神经反射模型、偏振成像、高光谱和AI线图技术。

## 推荐优先级

| 优先级 | 技术方向 | 对微痕/碑刻价值 | 成本 | 近期可做 |
| --- | --- | --- | --- | --- |
| 1 | 校准光度立体与近似平面细节恢复 | 直接输出法线/高度，最适合浅刻 | 中 | 是 |
| 2 | Multi-Light Image Collections + BRDF/法线优化 | 比传统RTI更准，适合复杂材质 | 中 | 是 |
| 3 | Neural RTI / Neural Relightable Images | 复杂反射重打光质量更高 | 高 | 先研究 |
| 4 | 多光谱/高光谱RTI | 同时看纹理、材料、褪色文字 | 高 | 小规模可试 |
| 5 | Shape from Polarization偏振成像 | 对高反光、低纹理表面有优势 | 中高 | 可做实验 |
| 6 | 3D扫描/摄影测量 + RTI融合 | 全局几何 + 局部微痕 | 中高 | 是 |
| 7 | AI线图/数字拓片生成 | 把增强图转研究用线图/拓片 | 中 | 是 |

## 方向一：校准光度立体

核心思想：固定相机，用已知位置的多光源拍摄，直接估计每个像素的表面法线，再进一步积分成高度图。

与RTI区别：
- RTI强调交互式重打光。
- 光度立体强调法线图、深度/高度图和定量表面重建。

为什么重要：
- 汉画像石、碑刻、甲骨、石经都接近“近似平面 + 细微起伏”。
- 微痕增强需要的不只是好看，而是稳定的表面方向和凹凸线索。
- 固定光源矩阵比手持H-RTI更适合复现公开资料中的“光源矩阵”路线。

重点资料：
- `papers/reading/04-photometric-stereo/18-DiLiGenT_Pi_Photometric_Stereo/18-DiLiGenT_Pi_Photometric_Stereo.pdf`
- `papers/reading/04-photometric-stereo/09-Photometric_Stereo_3D_Reconstruction_Artworks/09-Photometric_Stereo_3D_Reconstruction_Artworks.pdf`
- [Photometric Stereo Techniques for 3D Reconstruction of Paintings and Drawings, 2025](https://www.mdpi.com/2571-9408/8/4/129)

近期实验：
- 设计一个8-16灯位的固定光源矩阵。
- 对硬币、刻字石片、手工刻痕板做采集。
- 输出法线图、虚拟掠射光图、粗略高度图。
- 与RelightLab输出的RTI增强结果对比。

## 方向二：MLIC + BRDF/法线优化

MLIC（Multi-Light Image Collections）可以理解为RTI的现代数据基础：同一视角、多光照图像集合。现代研究不只拟合PTM/HSH，还会估计法线、BRDF和更可靠的渲染参数。

为什么重要：
- 传统RTI对粗糙石材、阴影、高光和非Lambertian表面处理有限。
- BRDF和法线优化能减少“看起来很清楚但其实是伪影”的风险。
- 对研究型微痕扫描来说，这比单纯增强对比度更可信。

重点资料：
- `papers/reading/05-frontier-reflectance-imaging/19-BRDF_Monotonicity_Shading_Normals/19-BRDF_Monotonicity_Shading_Normals.pdf`

近期实验：
- 把自采多光照照片作为MLIC保存，而不是只输出RTI文件。
- 同时保留几类法线图：几何分析用法线、视觉重打光用shading normal。
- 在数字拓片和线图生成时记录使用的是哪一种法线。

## 方向三：Neural RTI / 神经反射模型

核心思想：不再用PTM/HSH这种固定函数拟合每个像素，而是用神经网络学习“光照方向 -> 像素亮度/颜色”的映射。

优势：
- 能表达更复杂的反射、阴影和高光。
- 在相近存储成本下，重打光质量可能优于PTM/HSH。
- 新研究已开始关注Web端实时神经重打光。

风险：
- 训练和部署复杂。
- 可解释性弱于PTM/光度立体。
- 对第一阶段微痕复现不是必需，但很适合作为后续软件高阶方向。

重点资料：
- [DisK-NeuralRTI: Optimized NeuralRTI Relighting through Knowledge Distillation](https://iris.univr.it/handle/11562/1162371)
- [Efficient and user-friendly visualization of neural relightable images for cultural heritage applications](https://iris.cnr.it/handle/20.500.14243/532852)
- [Fast and accurate neural reflectance transformation imaging through knowledge distillation](https://arxiv.org/html/2510.24486v1)
- `repositories/github/NeuralRTI`
- `papers/reading/05-frontier-reflectance-imaging/32-NeuralRTI_and_Distillation/35-NeuralRTI_and_Distillation_note.md`

近期策略：
- 暂不作为第一版算法实现。
- 先保留原始MLIC数据，为未来训练Neural RTI准备。
- 后续可把Neural RTI作为高质量Web查看器方向。

## 方向四：多光谱/高光谱RTI

核心思想：RTI看表面几何和反射变化，多/高光谱看不同波段下的材料和颜色差异。二者结合后，可以同时观察“表面微地形”和“材料/色素/褪色信息”。

为什么重要：
- 汉画像石本身多为石刻，但可能存在颜料残留、污染、风化层、拓印墨迹。
- 碑刻和甲骨可能存在肉眼不明显的残留文字、污渍和材料差异。
- 微痕成像如果只看几何，可能漏掉材料层面的信息。

重点资料：
- `papers/reading/05-frontier-reflectance-imaging/22-Multispectral_RTI_Framework/22-Multispectral_RTI_Framework.pdf`
- [Integrating Spectral and RTI](https://jubilees.stmarytx.edu/integrating/)
- [Hyperspectral imaging and CNNs for ancient Egyptian artefacts, 2024](https://heritagesciencejournal.springeropen.com/articles/10.1186/s40494-024-01182-9)
- [Hyperspectral imaging for Neolithic rock painting analysis, 2023](https://heritagesciencejournal.springeropen.com/articles/10.1186/s40494-023-00940-5)

近期实验：
- 低成本先做“可见光 + 近红外改机/红外灯”的小实验。
- 记录同一光照角度下不同波段图像。
- 观察是否能区分刻痕、污染和石材纹理。

## 方向五：Shape from Polarization 偏振成像

核心思想：利用反射光的偏振信息恢复表面法线和局部细节。可以用偏振相机，也可以用普通相机加可旋转线偏振片做实验。

为什么重要：
- 对高反光、低纹理、传统摄影测量困难的表面有优势。
- 能补充RTI/光度立体在某些材质上的不足。
- 对小型碑刻、甲骨、硬币、石片实验样本有探索价值。

重点资料：
- `papers/reading/05-frontier-reflectance-imaging/20-Shape_From_Polarization_Heritage/20-Shape_From_Polarization_Heritage.pdf`
- `papers/reading/05-frontier-reflectance-imaging/21-Polarization_UNet_Surface_Normal/21-Polarization_UNet_Surface_Normal.pdf`
- [Shape reconstruction of heritage assets by polarization information, 2023](https://isprs-archives.copernicus.org/articles/XLVIII-M-2-2023/1653/2023/)

近期实验：
- 用线偏振片拍摄0/45/90/135度图像。
- 与普通斜光照片和RTI增强结果对比。
- 先用于小样本，不急于上真实文物。

## 方向六：3D扫描/摄影测量 + RTI融合

核心思想：用摄影测量、结构光、激光扫描或LiDAR获取全局几何，用RTI/光度立体获取局部微痕。

为什么重要：
- 汉画像石和碑刻常有较大尺寸，RTI擅长局部，不擅长整体三维。
- 3D模型可用于定位、测量和展示，RTI可用于识读和微痕研究。
- 公开微痕成像资料中也提到微痕成像、多光谱、高精度激光扫描和全信息模型的组合。

近期实验：
- 手机摄影测量/结构光扫描建立粗模型。
- 在关键局部做RTI采集。
- 在全信息模型中把RTI结果绑定到3D模型局部区域。

## 方向七：AI线图与数字拓片生成

核心思想：把RTI增强图、法线图、数字拓片、点云等输入AI或几何算法，自动生成研究用线图、轮廓图和辅助释读结果。

为什么重要：
- 汉画像石研究依赖线图和拓片。
- 手工线图耗时且风格不统一。
- AI可以作为辅助，但必须保留人工复核。

重点资料：
- [Relic2Contour, 2025](https://www.nature.com/articles/s40494-025-01606-0)
- [Automated generation of archeological line drawings from sculpture point cloud, 2025](https://www.nature.com/articles/s40494-025-01678-y)
- [Generating archaeological line drawings from limited reference images, 2026](https://www.nature.com/articles/s40494-026-02526-3)
- [cuneiform_lineart](https://github.com/laclark/cuneiform_lineart)
- `papers/reading/06-ai-annotation-line-drawing/25-Relic2Contour/24-Relic2Contour_note.md`
- `papers/reading/06-ai-annotation-line-drawing/26-Archaeological_Line_Drawings_Point_Cloud/25-Archaeological_Line_Drawings_Point_Cloud_note.md`
- `papers/reading/06-ai-annotation-line-drawing/34-Archaeological_Line_Drawings_Limited_References/33-Archaeological_Line_Drawings_Limited_References_note.md`

近期实验：
- 不直接训练大模型，先用OpenCV生成初步线图。
- 建立“增强图 -> 人工修正线图”的小数据集。
- 后续再尝试半监督或小样本微调。

## 推荐技术组合

### 第一阶段：近期可复现

```text
固定光源矩阵
  + 校准光度立体
  + RelightLab/RTI输出
  + 法线增强
  + 数字拓片/线图初稿
```

这是当前适合采用的路线：成本可控、理论清楚、能直接服务微痕扫描。

### 第二阶段：提高质量

```text
MLIC数据管理
  + BRDF/法线优化
  + 3D扫描局部绑定
  + 多输出层全信息模型
```

这一阶段解决可信度、可追溯和研究使用问题。

### 第三阶段：前沿探索

```text
Neural RTI
  + 多光谱/高光谱RTI
  + 偏振成像
  + AI线图/拓片生成
```

这一阶段目标是达到比传统RTI更强的材料识别、复杂反射表达和自动化分析能力。

## 项目结论

如果目标是“更好实现RTI微痕效果”，最值得优先投入的是：

1. **固定光源矩阵 + 校准光度立体**：直接解决微痕法线/高度问题。
2. **MLIC + 法线/BRDF优化**：让结果更可信，减少伪影。
3. **数字拓片和AI线图**：把增强结果转成研究者真正会用的图像。
4. **3D扫描融合**：解决汉画像石整体几何和局部微痕的关系。
5. **多光谱/偏振/Neural RTI**：作为第二阶段或第三阶段增强能力。

## 2026补充结论

新增资料显示，RTI/PTM正在从“交互查看工具”扩展为“计算分析数据源”：

- RTI图像可复用于SfM，把局部RTI登记回整体3D模型。
- RTI/HSH特征可进入深度学习聚类，用于碎片关系、纹样相似性和材料表面比较。
- NeuralRTI和DisK-NeuralRTI正在解决传统PTM/HSH复杂反射拟合不足和神经渲染速度问题。
- AI线图不再只有传统边缘检测，已经出现半监督GAN、点云几何特征线和LoRA/扩散模型三条路线。

对汉画像石而言，近期重点仍应是固定光源矩阵、光度立体、RTI增强图、人工线图和YOLO/SAM/IIML闭环。NeuralRTI、多光谱RTI、偏振和扩散线图作为前沿储备，但必须保留原始多光照图像和人工审核链。
