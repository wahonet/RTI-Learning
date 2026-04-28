# RTI论文与资料索引

本文件夹存放RTI、PTM、H-RTI、光度立体、文化遗产应用、汉画像石和微痕相关的公开PDF资料。阅读顺序见 `../tutorials/00-reading-plan.md`。

总学习路线见：

- `../learning-roadmap.html`
- `../learning-roadmap.md`
- `../research-master-index-2026.csv`

## 必读资料

1. `01_CHI_RTI_Highlight_Capture_Guide.pdf`
   - CHI官方H-RTI采集指南。
   - 学习重点：固定相机、反光球、光源移动、采集顺序、元数据。

2. `02_Earl_2011_RTI_Systems_Ancient_Documentary_Artefacts.pdf`
   - 古文献和考古对象RTI系统综述。
   - 学习重点：RTI作为文化遗产记录系统，而不仅是单个图像算法。

3. `03_Mudge_2006_RTI_Rock_Art_Multiple_Viewpoint.pdf`
   - Highlight RTI经典论文，岩画和多视角RTI。
   - 学习重点：手持光源、黑色反光球、野外采集。

4. `05_Palma_2010_Dynamic_Shading_Enhancement_RTI.pdf`
   - RTI动态增强渲染论文。
   - 学习重点：细节增强、动态光照优化、RTIViewer增强模式。

5. `06_RTI_Gravestone_Detail.pdf`
   - 墓碑文字和刻工细节RTI案例。
   - 学习重点：风化石刻、文字识读、specular enhancement。

6. `12_Han_Relief_From_Rubbing_Height_Map.pdf`
   - 利用拓片恢复汉画像浮雕效果。
   - 学习重点：拓片到高度图、低频/高频分解、数字拓片启发。

## 进阶资料

7. `04_Mudge_2005_RTI_Coins_Grand_St_Bernard.pdf`
   - 硬币RTI和结构光结合案例。
   - 适合学习RTI与3D扫描互补。

8. `07_RTI_in_Epigraphical_Studies.pdf`
   - 碑铭学RTI方法综述。
   - 适合理解RTI在碑刻释读中的研究价值。

9. `09_Photometric_Stereo_3D_Reconstruction_Artworks.pdf`
   - 光度立体与艺术品三维重建。
   - 适合进入法线图、高度图和定量重建方向。

10. `14_2_5D_Digitization_Oracle_Bone_Bamboo_Slip_RTI.pdf`
    - 甲骨、竹简2.5D数字化讲义。
    - 适合迁移到浅刻文字和汉画像石场景。

## 工具资料

11. `15_CHI_RTIViewer_User_Guide_v1_1.pdf`
    - RTIViewer官方用户指南。
    - 学习重点：查看、增强模式、法线可视化、书签。

12. `16_CHI_RTI_Glossary_v1.pdf`
    - CHI官方RTI术语表。
    - 适合整理中文术语。

13. `17_Tutorial_Installing_RTIViewer_RTIBuilder.pdf`
    - RTIViewer和RTIBuilder安装教程。
    - 适合工具安装参考。

## 前沿技术资料

14. `18_DiLiGenT_Pi_Photometric_Stereo_Near_Planar_Rich_Details_ICCV2023.pdf`
    - 近似平面丰富细节的光度立体基准，直接对应碑刻、浅浮雕、微痕场景。

15. `19_BRDF_Monotonicity_Shading_Normals_MLIC_GCH2024.pdf`
    - MLIC、BRDF和法线优化，适合研究如何减少RTI/光度立体伪影。

16. `20_Shape_From_Polarization_Cultural_Heritage_2024.pdf`
    - 偏振成像用于文化遗产高分辨率表面重建。

17. `21_Polarization_UNet_Surface_Normal_2024.pdf`
    - 深度学习偏振法线估计，作为偏振成像进阶方向。

18. `22_Multispectral_RTI_Integrated_Angular_Spectral_Reflectance.pdf`
    - 多光谱RTI，把角度反射和波段信息结合起来。

## 2024-2026新增跟踪资料

19. `28_RTI_Heritage_Timbers_2025.pdf`
    - 低成本手持RTI dome用于历史木构节疤检测，并把RTI图像用于SfM。
    - 阅读笔记：`notes/28_RTI_Heritage_Timbers_2025.md`

20. `notes/23_Han_Portrait_Stone_YOLOv5_2024.md`
    - 汉画像石人物目标检测，增强YOLOv5，类别包括伏羲女娲和乐舞人物。
    - PDF直链下载中断，保留网页阅读笔记。

21. `notes/24_Relic2Contour_2025.md`
    - 半监督GAN生成文物轮廓线图，适合数字拓片和研究线图方向。

22. `notes/25_Archaeological_Line_Drawings_Point_Cloud_2025.md`
    - 从石雕点云自动提取考古线图，适合3D扫描/光度立体高度图路线。

23. `notes/26_Photometric_Stereo_Paintings_Drawings_2025.md`
    - 定制拍摄架和精确灯位测量提高光度立体重建稳定性。

24. `notes/27_Close_Range_Photogrammetry_RTI_Tiryns_2025.md`
    - 近景摄影测量与RTI结合，形成2.5D文物记录。

25. `notes/29_Virtual_RTI_Egyptian_Chapel_2024.md`
    - V-RTI用于传统RTI难以采集的狭窄浅浮雕空间。

26. `notes/30_Quantitative_RTI_Profilometry_2024.md`
    - RTI normal map和法线积分用于半平面轮廓测量的定量评估。

27. `notes/31_Multispectral_RTI_Framework.md`
    - 多光谱RTI，把光照方向和波段信息结合。

28. `notes/32_Beyond_Relighting_RTI_Textiles_2026.md`
    - RTI/HSH特征和深度学习用于文物碎片聚类，说明RTI可进入AI分析。

29. `notes/33_Archaeological_Line_Drawings_Limited_References_2026.md`
    - 用扩散模型和LoRA在有限参考图像下生成考古线图。

30. `notes/34_3D_Digital_Modeling_Han_Stone_Reliefs_2023.md`
    - 汉画像石三维数字建模保护与活化流程。

31. `notes/35_Neural_RTI_and_Distillation.md`
    - NeuralRTI、DisK-NeuralRTI、Neural Reflectance Field RTI资料综合。

32. `notes/36_ICON_Iconology_Ontology.md`
    - ICON图像学本体、图像志/图像学语义表达和IIML映射。

## 暂未直接下载但需要继续跟踪

- Malzbender et al. 2001, `Polynomial Texture Maps`：经典PTM论文，在线文本可读，后续继续寻找稳定PDF源。
- Malzbender et al. 2001, `Polynomial Texture Map (.ptm) File Format`：PTM格式规范，后续补PDF。
- Earl et al., `Archaeological applications of polynomial texture mapping`：CORE源不稳定，后续继续补充。
- `Application of Reflectance Transformation Imaging to Experimental Archaeology Studies`：MDPI页面可读，PDF下载被站点拦截，后续可手动补。
- `3D Digital Modeling as a Sustainable Conservation and Revitalization Path for Han Dynasty Stone Reliefs`：MDPI页面可读，PDF下载被站点拦截，后续可手动补。
- `Automating RTI: Automatic light direction detection...`：Exeter页面可读，PDF直链下载异常，后续继续补。
- `A quantitative approach to RTI in profilometric applications`：Springer/INRiM页面可读，PDF直链下载异常，后续继续补。
- `Human figure detection in Han portrait stone images via enhanced YOLO-v5`：Nature页面可读，PDF下载中断，后续继续补。
- `Relic2Contour`、`Automated generation of archeological line drawings from sculpture point cloud`、`Generating archaeological line drawings from limited reference images`：Nature页面可读，PDF直链在本机返回不可读文件或下载中断，后续继续补。
