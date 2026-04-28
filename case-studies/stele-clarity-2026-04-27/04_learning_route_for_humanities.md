# 文科背景学习石刻精细采集：路线与时间表

## 先回答你的问题

需要一点理工基础，但不需要你先变成程序员、工程师或数学专业学生。  
你真正需要的是四类能力：

1. **摄影与光线**：知道曝光、焦距、景深、RAW、斜光、偏振为什么影响读字。
2. **三维采集直觉**：理解照片如何变成点云/网格，误差从哪里来。
3. **数据管理**：文件命名、备份、元数据、版本、坐标、尺度，保证别人能复核。
4. **软件操作与判断**：能用 RTI/摄影测量/点云软件做出结果，并知道结果可信不可信。

数学和编程可以后置。你前 3 个月的目标不是“懂算法公式”，而是能稳定采一块碑、处理一组数据、解释哪里可靠哪里不可靠。

## 总学习目标

6 个月达到：

- 能独立设计一套碑刻/画像石采集方案。
- 能拍摄合格的多光照和摄影测量照片。
- 能用 Meshroom/Metashape/COLMAP 做基础 3D 模型。
- 能用 RTI/relight/OpenLIME 生成可交互重光照结果。
- 能用 CloudCompare/MeshLab/GigaMesh 做基础查看、清理、截面、曲率/阴影增强。
- 能把图像、模型、释文、字框、疑字组织成可交付资料包。

## 第一阶段：摄影和采集基础，2-3 周

### 你要学会

- 光圈、快门、ISO、曝光补偿。
- 焦距、透视、景深。
- RAW、白平衡、灰卡、色卡。
- 为什么树影、反光、水印会毁掉后续处理。
- 斜光、漫射光、交叉偏振的作用。

### 练习

- 找一块硬币、砖、石头或有浅刻字的物体。
- 固定手机/相机，从 8 个方向打光拍摄。
- 比较左光、右光、上光、下光时细节变化。
- 练习不改变构图，只改变光线。

### 推荐资料

- 《Understanding Exposure》（Bryan Peterson）：摄影曝光入门。
- Cambridge/Arc Humanities 的 **Digital Techniques for Documenting and Preserving Cultural Heritage**：先看目录和 RTI、Photogrammetry、Structured Light 几章，不必一口气读完。
- Cultural Heritage Imaging 的 RTI capture guide。

### 时间投入

每周 5-7 小时，2 周能入门；第 3 周用来实拍小样。

## 第二阶段：RTI / 多光照读字，3-4 周

### 你要学会

- 什么是 RTI、H-RTI、反光球、光源方向。
- 固定相机、变光源的拍摄规范。
- RTI 输出和普通照片的区别。
- 如何判断一组 RTI 数据是否失败：相机动了、光照不足、反光球太小、曝光不一致、阴影遮挡。

### 练习

- 对同一个浅刻对象拍 24 张光照图。
- 尝试用 relight 或 RTIBuilder/RTIViewer 生成可交互结果。
- 输出几张最利于读字的“虚拟侧光图”。
- 让另一个人只看输出图，记录是否多读出笔画。

### 推荐资料

- Cultural Heritage Imaging：RTI Highlight Capture Guide。
- Mytum et al.：RTI in Historical Archaeology。
- Herculaneum graffiti RTI 论文。
- `relight` 和 `OpenLIME` 项目文档。

### 时间投入

每周 6-8 小时，3 周能做第一个合格小样；第 4 周做真实碑刻试采。

## 第三阶段：摄影测量与三维模型，4-6 周

### 你要学会

- SfM/MVS 是什么：多张照片 -> 相机位置 -> 点云 -> 网格 -> 纹理。
- 拍摄重叠率、环绕角度、尺度尺、标靶。
- 稀疏点云、稠密点云、网格、纹理、正射影像的区别。
- 为什么平面碑不好建深度，为什么需要斜拍和边缘信息。

### 练习

- 用一个小石刻/砖/雕塑拍 80-150 张照片。
- 用 Meshroom 或 Metashape 跑出 3D 模型。
- 用 CloudCompare 查看点云，用 MeshLab 查看网格。
- 在模型上做测距、截面、无纹理渲染。

### 推荐资料

- Historic England：Photogrammetric Applications for Cultural Heritage。
- 《Photogrammetry for Archaeological Objects: A Manual》。
- `Meshroom` 官方文档和示例。
- `COLMAP` 官方 Getting Started。
- CloudCompare wiki。

### 时间投入

每周 6-10 小时。第 1-2 周做小物件，第 3-4 周做一块小碑/局部，第 5-6 周整理参数和失败经验。

## 第四阶段：3D 后处理与数字拓片，4-6 周

### 你要学会

- 点云和网格清理。
- 法线、曲率、环境遮蔽、radiance scaling 的基本含义。
- 什么是局部参考面，为什么数字拓片依赖凹凸深度。
- 如何从 3D 模型生成读字友好的渲染图。

### 练习

- 在 MeshLab/CloudCompare 中查看无纹理模型。
- 尝试环境遮蔽、法线、曲率或阴影增强。
- 安装并试用 GigaMesh，用示例数据理解微表面提取。
- 选一块文字区域，输出“类似拓片”的灰度/黑白图。

### 推荐资料

- Digital stone rubbing from 3D models。
- npj Heritage Science 2025：3D fine model rubbing extraction。
- GigaMesh Manual 和 tutorials。
- MeshLab/CloudCompare 教程。

### 时间投入

每周 6-8 小时，4 周能理解流程；如果要写自己的数字拓片算法，再加 1-2 个月。

## 第五阶段：结构化、标注和 AI 识读，3-4 周

### 你要学会

- 如何把一块碑拆成区域、列、行、字框。
- 如何记录疑字、缺字、候选字、置信度。
- 什么是 OCR 候选，什么是人工校读定稿。
- 如何让 AI 使用上下文，而不是直接相信图像识别。

### 练习

- 给一块碑建立 CSV/JSON 标注表。
- 对每个字框保存图像坐标、增强图坐标、人工释读。
- 用 OCR/视觉大模型生成候选，再人工校对。
- 把最终释文、疑字、图片证据、坐标一起保存。

### 推荐资料

- PaddleOCR PP-StructureV3 文档。
- TEI/EpiDoc 入门资料。
- Ithaca 论文：学习“模型给候选，专家做判断”的协作范式。

### 时间投入

每周 5-7 小时，3-4 周能建立第一个可复核数据包。

## 6 个月时间表

### 第 1 月：摄影 + RTI 入门

目标：用低成本设备拍出一组多光照数据，并能明显看出斜光对浅刻的帮助。

交付物：

- 一个小物件 RTI 样例。
- 一块碑的 8-16 方向斜光照片。
- 一份现场记录模板。

### 第 2 月：真实碑刻 RTI 采集

目标：对 3-5 块碑做标准化多光照采集。

交付物：

- 每块碑的整体照、局部照、多光照组。
- 每块碑的最佳读字侧光图。
- 失败原因记录。

### 第 3 月：摄影测量建模

目标：能从照片生成一块碑或一个石刻局部的 3D 模型。

交付物：

- Meshroom/Metashape 项目文件。
- 点云、网格、纹理、正射图。
- 一页误差和可读性评价。

### 第 4 月：3D 增强和数字拓片

目标：从 3D 模型生成更利于读字的可视化图。

交付物：

- 环境遮蔽图、曲率图、伪拓片图。
- 字迹区域对比图：普通照片 vs RTI vs 3D 渲染。
- 一份“哪种图最有助于读字”的评估表。

### 第 5 月：标注和 AI 候选

目标：把图像证据和文字释读绑定。

交付物：

- 字框/列/行标注表。
- OCR/AI 候选表。
- 人工确认、疑字、缺字记录。

### 第 6 月：形成可复用流程

目标：形成一个可以用于后续批量碑刻的 SOP。

交付物：

- 采集 SOP。
- 文件命名规范。
- 数据备份规范。
- 释文结构化模板。
- 1-2 个完整碑刻案例。

## 每周学习安排模板

如果你每周能拿出 6 小时：

- 2 小时读资料/看教程。
- 2 小时软件操作。
- 1 小时实拍或整理素材。
- 1 小时写采集日志和问题清单。

如果你每周能拿出 10 小时：

- 3 小时读资料。
- 3 小时软件操作。
- 2 小时实拍。
- 2 小时整理数据、写报告、做对比图。

## 对文科生最重要的提醒

1. **不要从公式开始**。先从拍摄规范、可复核数据和读字效果开始。
2. **不要把软件结果当真相**。三维模型、RTI、数字拓片都是解释工具，要保留原始数据。
3. **你有优势**。你知道什么信息有历史价值，懂释读、文献、语境和不确定性表达，这是纯技术人员不容易替代的。
4. **找一个理工合作者会加速很多**。你负责问题定义、采集规范、释读评价；对方负责算法、脚本、批处理。
5. **最好的学习方式是做一个小型案例**。先完整做一块碑，比泛泛学十门课更有效。

## 参考书和教程清单

### 免费优先

- Cultural Heritage Imaging：RTI Guide to Highlight Image Capture。
- Historic England：Photogrammetric Applications for Cultural Heritage。
- Library of Congress PDF：Digital Techniques for Documenting and Preserving Cultural Heritage。
- GigaMesh Manual。
- Meshroom 官方文档。
- COLMAP 官方文档。
- CloudCompare wiki。
- MeshLab 官方文档和 YouTube 教程。

### 纸质/系统书

- Jon Bedford, **Photogrammetric Applications for Cultural Heritage**。
- Matthew L. Vincent et al., **Photogrammetry for Archaeological Objects: A Manual**。
- Fabio Remondino and Efstratios Stylianidis, **3D Recording, Documentation and Management of Cultural Heritage**。
- Anna Bentkowska-Kafel and Lindsay MacDonald, **Digital Techniques for Documenting and Preserving Cultural Heritage**。
- Bryan Peterson, **Understanding Exposure**。

## 最小知识树

```text
碑刻学/画像石研究问题
  -> 摄影基础
     -> 曝光、焦距、景深、RAW、色彩管理
  -> 光照与材质
     -> 斜光、漫射、反光、偏振、阴影
  -> 多光照成像
     -> RTI、photometric stereo、法线图
  -> 三维采集
     -> 摄影测量、点云、网格、纹理、尺度
  -> 三维后处理
     -> 清理、配准、曲率、环境遮蔽、数字拓片
  -> 文字结构化
     -> 区域、列、行、字框、候选、疑字、缺字
  -> AI 辅助
     -> OCR 候选、上下文校读、知识库/RAG
```

