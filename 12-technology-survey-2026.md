# 12 RTI/PTM与汉画像石技术调研 2026

本文汇总本轮新增资料，重点回答三个问题：

1. RTI/PTM在考古、文博、碑刻、浅浮雕中的新应用是什么。
2. 除RTI/PTM外，哪些新技术适合汉画像石图像学、形相学和微痕研究。
3. YOLO、SAM、线图生成、IIML/图像学本体如何进入汉画像石结构化工作流。

## 总体判断

传统RTI/PTM仍然重要，但不应作为终点。对汉画像石最有价值的路线是：

```text
多光照原始图像 MLIC
  -> RTI/PTM/HSH/RBF交互重打光
  -> 光度立体法线图/高度图
  -> 数字拓片/线图
  -> YOLO/SAM候选标注
  -> IIML/图像学知识库
```

其中MLIC原始数据必须保存。未来NeuralRTI、DisK-NeuralRTI、RTI特征聚类、神经线图生成都依赖原始多光照图像，而不是只依赖最终PTM文件。

## 1. RTI/PTM新应用

### 1.1 低成本便携RTI dome

2025年历史木构节疤检测论文展示了手持低成本RTI dome的价值。它用于木梁表面节疤检测，并把RTI图像复用于SfM三维重建。对汉画像石而言，这说明现场不可移动文物可以采用便携灯阵，局部RTI还可以配准回整体3D模型。

参考：

- `papers/28_RTI_Heritage_Timbers_2025.pdf`
- `papers/notes/28_RTI_Heritage_Timbers_2025.md`

### 1.2 V-RTI

V-RTI通过三维模型模拟多方向虚拟光照，适合狭窄空间、不可布光场景和已有高质量3D模型的对象。它不能替代真实RTI，但可作为无法多光照采集时的补救方案。

参考：

- `papers/notes/29_Virtual_RTI_Egyptian_Chapel_2024.md`

### 1.3 RTI不只用于观看，也用于计算

2026年RTI纺织品碎片聚类论文把RTI/HSH数据作为深度特征输入，用于碎片关系聚类。这对汉画像石非常关键：RTI可以用于相似纹样检索、残石拼合、图像元素聚类，而不只是RTIViewer里的交互观察。

参考：

- `papers/notes/32_Beyond_Relighting_RTI_Textiles_2026.md`

## 2. 光度立体与定量表面

RTI强调视觉重打光，光度立体强调法线、高度和定量表面。汉画像石、碑刻、甲骨、竹简都属于“近似平面 + 细微起伏”，因此固定光源矩阵和光度立体应成为第一阶段实验重点。

2025年绘画/绘图光度立体论文强调精确测量灯位、相机和采集平面的相对位置，以降低法线积分误差。2024年RTI profilometry论文则提醒：从RTI normal map积分得到高度图，需要和轮廓仪、激光扫描、摄影测量等方法做定量比较。

参考：

- `papers/notes/26_Photometric_Stereo_Paintings_Drawings_2025.md`
- `papers/notes/30_Quantitative_RTI_Profilometry_2024.md`
- `papers/18_DiLiGenT_Pi_Photometric_Stereo_Near_Planar_Rich_Details_ICCV2023.pdf`

近期实验建议：

- 自制刻痕标定板，包含不同线宽和深度。
- 用8-16灯位固定灯阵采集。
- 同时输出RTI、法线图、虚拟斜光图和高度图。
- 与传统拓片/手绘线图比较。

## 3. Neural RTI与神经重光照

NeuralRTI用神经网络替代PTM/HSH固定基函数，能更好拟合复杂反射、高光和阴影。DisK-NeuralRTI进一步用知识蒸馏压缩decoder，使神经RTI接近Web实时浏览。2025年的Neural Reflectance Field RTI把像素位置、光照方向和局部反射潜变量结合，进一步提升复杂表面拟合能力。

对本项目的策略：

- 第一阶段不把NeuralRTI作为主工具。
- 必须保存MLIC原始数据，为后续训练预留可能。
- 用`repositories/github/NeuralRTI`先跑通示例。
- 未来比较PTM/HSH/RBF/NeuralRTI在石刻样本上的差异。

参考：

- `repositories/github/NeuralRTI`
- `repositories/github/NeuralRTI_NOTE.md`
- `papers/notes/35_Neural_RTI_and_Distillation.md`

## 4. 多光谱、偏振与材料信息

多光谱RTI把光照方向和波段结合，可同时观察表面形态和材料差异。对汉画像石而言，它可能用于区分刻痕、裂缝、污染、拓印墨迹、颜料残留和修复痕迹。

偏振成像则适合高反光、低纹理或传统摄影测量困难的表面。它不是第一阶段必需，但可作为小样本实验方向。

参考：

- `papers/22_Multispectral_RTI_Integrated_Angular_Spectral_Reflectance.pdf`
- `papers/notes/31_Multispectral_RTI_Framework.md`
- `papers/20_Shape_From_Polarization_Cultural_Heritage_2024.pdf`
- `papers/21_Polarization_UNet_Surface_Normal_2024.pdf`

## 5. 汉画像石YOLO与目标检测

2024年汉画像石增强YOLOv5论文是目前最直接的“汉画像石 + YOLO”资料。其数据集包含伏羲女娲和乐舞人物两类，训练/验证/测试共285张。论文说明Coordinate Attention对复杂背景下的人物检测提升最明显。

对本项目的启发：

- 第一版不要追求完整图像学体系，先做少量高价值类别。
- bbox用于粗定位，多边形和线段用于研究标注。
- RTI增强图、拓片、线图和原图要分开标注并记录版本。

建议第一批类别：

- 伏羲女娲。
- 乐舞人物。
- 车马。
- 神兽。
- 建筑构件。
- 铭文/榜题。

参考：

- `papers/notes/23_Han_Portrait_Stone_YOLOv5_2024.md`

## 6. SAM、多边形与IIML

SAM适合从点、框或文本提示生成候选mask，但汉画像石中的浅刻、拓片噪声和石材纹理容易造成伪轮廓。建议流程是：

```text
YOLO粗框
  -> SAM候选多边形
  -> 人工修正
  -> IIML标注
  -> 图像学关系和解释
```

IIML中应记录：

- 资源版本：原图、RTI增强图、法线图、线图、拓片。
- 几何类型：bbox、polygon、line、trace。
- 生成方式：manual、yolo、sam、line-extraction。
- 审核状态：candidate、reviewed、rejected。
- 解释层级：前图像、图像志、图像学。

## 7. 自动线图与数字拓片

线图方向分为三条路线：

### 7.1 二维图像到线图

Relic2Contour使用半监督GAN，从有病害和噪声的文物图像中生成更清晰的轮廓。2026年有限参考图像线图论文则使用FLUX.1 Kontext和LoRA进行小样本微调。

参考：

- `papers/notes/24_Relic2Contour_2025.md`
- `papers/notes/33_Archaeological_Line_Drawings_Limited_References_2026.md`

### 7.2 点云到线图

2025年考古线图点云论文使用加权质心投影提取石雕点云特征线，适合有3D扫描、摄影测量或光度立体高度图的对象。

参考：

- `papers/notes/25_Archaeological_Line_Drawings_Point_Cloud_2025.md`

### 7.3 考古出版图工具

Ceramatic2.0展示了“AI识别 + 标准化考古绘图输出”的工程方向，虽然对象是陶器，但其自动化出版图流程值得借鉴。

参考：

- `repositories/README.md`

## 8. 图像学、形相学和知识库

ICON Ontology提供了图像学解释建模的成熟参考。对汉画像石而言，应该把标注分为：

- 几何层：点、线、框、多边形。
- 前图像层：人物、动物、器物、建筑、纹样。
- 图像志层：伏羲女娲、乐舞百戏、车马出行、升仙等主题。
- 图像学层：墓葬礼仪、宇宙观、祥瑞、身份和地域风格解释。

这与本项目`10-iiml-knowledge-base.md`和`iiml-jsonld.schema.json`一致，但后续需要补充解释层级、证据资源、研究者和模型来源字段。

参考：

- `papers/notes/36_ICON_Iconology_Ontology.md`
- `10-iiml-knowledge-base.md`

## 9. 推荐实施路线

### 第一阶段：可立即做

- 整理已有论文和仓库。
- 跑通RelightLab/RTIViewer/OpenLIME基础流程。
- 自采硬币、刻痕板、石片、拓片样本。
- 输出RTI、法线图、虚拟斜光图、数字拓片初稿。
- 建立小规模YOLO标注集。

### 第二阶段：研究型增强

- 固定光源矩阵。
- 光度立体高度/法线实验。
- RTI与SfM配准。
- SAM辅助多边形标注。
- IIML/JSON-LD导出。

### 第三阶段：前沿探索

- NeuralRTI和DisK-NeuralRTI。
- 多光谱RTI。
- 偏振成像。
- RTI特征聚类和相似纹样检索。
- LoRA/扩散模型生成考古线图。

## 10. 当前资料缺口

- 汉画像石公开标注数据集仍未找到稳定下载源。
- Relic2Contour、2026考古线图等新论文代码尚未找到或未成功下载。
- OpenLIME和Relight大仓库因网络问题未完整下载，需要后续补。
- 需要补充更多中文“形相学”原始论文和汉画像石图像学资料。
- 需要建立真实样本采集和标注闭环。
