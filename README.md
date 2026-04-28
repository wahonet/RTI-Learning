# RTI Learning

本仓库用于整理 RTI、光度立体、三维采集、数字拓片、碑刻识读和汉画像石结构化相关资料。重点是文物表面浅刻、低浮雕、风化纹理、榜题和图像内容的采集、处理、标注与结构化。

仓库分为两部分：

- 基础学习：RTI 原理、采集方法、处理工具、论文和硬件方案。
- 应用案例：碑刻照片采集复盘、汉画像石结构化、YOLO 目标检测入门。
- 前沿调研：2024-2026 年 RTI/PTM、光度立体、Neural RTI、自动线图、YOLO/SAM 标注和图像学知识库资料。

## 合并记录

2026-04-28，原 `relics-align2` 项目中的碑刻和汉画像石资料已合并到本仓库。案例目录为：

[case-studies/stele-clarity-2026-04-27](case-studies/stele-clarity-2026-04-27)

原始碑刻照片和处理输出图没有纳入 GitHub。原因是原图带经纬度水印，文件体积也较大。仓库中保留文档、来源索引、脚本和复现实验说明。

## 学习顺序

1. [01-theory.md](01-theory.md)
   先了解 RTI、PTM、HSH、光度立体、法线图等基础概念。

2. [02-cultural-heritage-cases.md](02-cultural-heritage-cases.md)
   了解 RTI 在碑刻、墓碑、陶器、浅浮雕等文化遗产案例中的用途。

3. [03-toolchain-and-datasets.md](03-toolchain-and-datasets.md)
   熟悉 RTIViewer、RTIBuilder、OpenLIME、relight 等工具和公开数据。

4. [06-capture-sop.md](06-capture-sop.md) 与 [09-hardware-purchase-list.md](09-hardware-purchase-list.md)
   对应现场采集准备，包括相机、光源、三脚架、反光球、比例尺和文件命名。

5. [04-han-stone-reliefs.md](04-han-stone-reliefs.md) 与 [05-microtrace-reproduction.md](05-microtrace-reproduction.md)
   面向汉画像石、碑刻、拓片恢复、数字拓片和微痕成像。

6. [10-iiml-knowledge-base.md](10-iiml-knowledge-base.md) 与 [iiml-jsonld.schema.json](iiml-jsonld.schema.json)
   面向图像标注、知识图谱、结构化数据和 AI 辅助识读。

## 文档目录

- [01-theory.md](01-theory.md)：RTI、PTM、HSH、RBF、光度立体、法线图。
- [02-cultural-heritage-cases.md](02-cultural-heritage-cases.md)：文化遗产案例。
- [03-toolchain-and-datasets.md](03-toolchain-and-datasets.md)：工具链和公开数据。
- [04-han-stone-reliefs.md](04-han-stone-reliefs.md)：汉画像石、拓片和中文石刻资料。
- [05-microtrace-reproduction.md](05-microtrace-reproduction.md)：微痕成像、数字拓片和 AI 识读。
- [06-capture-sop.md](06-capture-sop.md)：碑刻和画像石采集规范草稿。
- [07-software-workflow.md](07-software-workflow.md)：软件流程和数据结构设想。
- [08-frontier-technologies.md](08-frontier-technologies.md)：前沿技术资料。
- [09-hardware-purchase-list.md](09-hardware-purchase-list.md)：采集设备清单。
- [10-iiml-knowledge-base.md](10-iiml-knowledge-base.md)：图像标注、知识图谱和 JSON-LD。
- [11-merged-project-map.md](11-merged-project-map.md)：项目合并说明。
- [12-technology-survey-2026.md](12-technology-survey-2026.md)：2024-2026 年 RTI/PTM、汉画像石、YOLO、线图生成和图像学本体调研。
- [learning-roadmap.html](learning-roadmap.html)：可浏览的RTI/PTM与汉画像石学习路线图，含论文、仓库、硬件和实验计划。
- [learning-roadmap.md](learning-roadmap.md)：学习路线入口说明。
- [missing-materials-2026.md](missing-materials-2026.md)：缺失PDF、仓库、数据集和硬件资料补齐清单。
- [papers/notes](papers/notes)：新增论文阅读笔记。
- [repositories](repositories)：GitHub 工具仓库快照和复现入口。
- [research-inventory-2026.csv](research-inventory-2026.csv)：本轮新增论文、仓库、下载状态和阅读笔记清单。
- [research-master-index-2026.csv](research-master-index-2026.csv)：目前为止的论文、仓库、数据集、硬件总索引。

## 案例目录

- [case-studies/stele-clarity-2026-04-27](case-studies/stele-clarity-2026-04-27)：碑刻照片采集复盘、重新采集路线、汉画像石结构化和 YOLO 学习路线。

## 英文资料处理

英文资料按以下顺序处理：

1. 标题、摘要、图注、结论先翻译。
2. 设备、采集流程、软件参数、数据格式优先整理。
3. 关键词建立中英文对照表。
4. 每篇资料形成一页中文摘要，包括研究对象、方法、设备、流程、可借鉴内容和未理解问题。

详细路线见：

[tutorials/08-chinese-first-learning-route.md](tutorials/08-chinese-first-learning-route.md)

## 数据原则

- 保留原始数据，不只保存处理图。
- 记录采集条件和处理参数。
- AI 结果作为候选，不作为最终释读。
- 公开数据前处理 GPS、馆藏限制和版权问题。
