# RTI阅读与学习计划

## 总目标

用4个阶段系统掌握RTI技术，再进入汉画像石和微痕复现方向：

1. 理解RTI/PTM/H-RTI的理论和采集逻辑。
2. 阅读文化遗产案例，判断RTI适合解决哪些问题。
3. 跑通工具链和公开数据集，形成实验记录。
4. 把RTI方法迁移到汉画像石、碑刻和微痕成像复现。

## 阶段一：RTI基础理论

建议时间：2-3天

阅读顺序：
1. `../papers/reading/01-rti-ptm-foundations/16-CHI_RTI_Glossary/16-CHI_RTI_Glossary.pdf`
2. `../papers/reading/01-rti-ptm-foundations/01-CHI_RTI_Highlight_Capture_Guide/01-CHI_RTI_Highlight_Capture_Guide.pdf`
3. `../papers/reading/01-rti-ptm-foundations/02-RTI_Systems_Ancient_Documentary_Artefacts/02-RTI_Systems_Ancient_Documentary_Artefacts.pdf`

学习目标：
- 解释RTI、PTM、H-RTI、法线图、反光球、光照方向。
- 理解为什么相机和对象必须固定。
- 理解为什么多角度光照能揭示浅刻和微痕。

输出任务：
- 整理一份中英术语表。
- 画出RTI采集到查看的流程图。
- 写出H-RTI采集的关键风险点。

## 阶段二：经典方法和增强显示

建议时间：3-4天

阅读顺序：
1. `../papers/reading/01-rti-ptm-foundations/03-Mudge_2006_RTI_Rock_Art/03-Mudge_2006_RTI_Rock_Art.pdf`
2. `../papers/reading/01-rti-ptm-foundations/05-Dynamic_Shading_Enhancement_RTI/05-Dynamic_Shading_Enhancement_RTI.pdf`
3. `../papers/reading/01-rti-ptm-foundations/15-CHI_RTIViewer_User_Guide/15-CHI_RTIViewer_User_Guide.pdf`

学习目标：
- 理解Highlight RTI如何用反光球恢复光照方向。
- 理解RTIViewer中的增强模式为什么能突出细节。
- 区分“交互重打光”和“生成固定增强图”。

输出任务：
- 写出手持光源法的采集步骤。
- 总结RTIViewer中最重要的增强模式。
- 建立“增强模式 -> 适合观察的问题”对照表。

## 阶段三：碑刻、文字和浅表面案例

建议时间：4-5天

阅读顺序：
1. `../papers/reading/02-heritage-epigraphy-cases/06-RTI_Gravestone_Detail/06-RTI_Gravestone_Detail.pdf`
2. `../papers/reading/02-heritage-epigraphy-cases/07-RTI_Epigraphical_Studies/07-RTI_Epigraphical_Studies.pdf`
3. `../papers/reading/02-heritage-epigraphy-cases/04-Mudge_2005_RTI_Coins_Grand_St_Bernard/04-Mudge_2005_RTI_Coins_Grand_St_Bernard.pdf`
4. `../papers/reading/02-heritage-epigraphy-cases/14-Oracle_Bone_Bamboo_Slip_RTI/14-Oracle_Bone_Bamboo_Slip_RTI.pdf`

学习目标：
- 理解RTI在墓碑、碑铭、硬币、甲骨和竹简中的作用。
- 判断RTI什么时候能替代传统照片，什么时候只是辅助。
- 建立碑刻和汉画像石的相似问题清单。

输出任务：
- 为每篇案例写300字摘要。
- 列出RTI适合/不适合的文物表面类型。
- 设计第一版汉画像石RTI采集需求。

## 阶段四：微痕、数字拓片和软件化

建议时间：5-7天

阅读顺序：
1. `../papers/reading/03-han-stone-reliefs-3d/12-Han_Relief_From_Rubbing_Height_Map/12-Han_Relief_From_Rubbing_Height_Map.pdf`
2. `../papers/reading/04-photometric-stereo/09-Photometric_Stereo_3D_Reconstruction_Artworks/09-Photometric_Stereo_3D_Reconstruction_Artworks.pdf`
3. `../docs/04-han-stone-ai/05-microtrace-reproduction.md`
4. `../docs/02-capture-hardware/06-capture-sop.md`
5. `../docs/03-software-data/07-software-workflow.md`

学习目标：
- 理解拓片恢复、RTI和光度立体之间的关系。
- 把公开资料中的“微痕成像”映射到公开RTI技术。
- 明确数字拓片、灰度图、线图、增强图的定义。

输出任务：
- 写一份“RTI -> 微痕增强”的技术映射表。
- 设计第一套低成本光源矩阵方案。
- 设计数字拓片的输入、处理和输出格式。

## 第一轮学习验收

完成以下内容后，进入实验复现：

- 能口头解释RTI、PTM、H-RTI和光度立体的区别。
- 能独立写出H-RTI采集步骤。
- 能说清楚RTI对碑刻/汉画像石的价值和局限。
- 能列出至少3种增强输出：增强图、法线图、数字拓片/线图。
- 能选择一套工具链：RelightLab + RTIViewer/OpenLIME。
