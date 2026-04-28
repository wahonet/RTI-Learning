# RTI Learning

这个仓库是我整理 RTI、光度立体、三维采集、数字拓片和汉画像石结构化资料的地方。最开始只是想把 RTI 学明白，后来发现碑刻、画像石、浅浮雕、微痕成像这些问题其实都绕不开同一件事：怎样把文物表面那些很浅、很细、肉眼不稳定可见的信息采下来，并且能让别人复核。

目前仓库里有两条线：

- 一条是基础学习：RTI 是什么，怎么拍，怎么处理，常用软件有哪些。
- 一条是应用问题：碑刻文字为什么普通照片后期救不回来，汉画像石图像怎样做标注、检索和结构化。

## 最近整理

2026-04-28，我把原来 `relics-align2` 里的碑刻和汉画像石资料合并到了这里。合并后的案例放在：

[case-studies/stele-clarity-2026-04-27](case-studies/stele-clarity-2026-04-27)

旧项目里有一些原始碑刻照片和处理输出图，因为带经纬度水印，体积也比较大，我没有放进 GitHub。仓库里主要保留文字资料、链接索引、脚本和复现实验说明。

## 我现在的学习顺序

如果从零开始，我会按这个顺序读：

1. 先看 [01-theory.md](01-theory.md)
   目标不是记公式，而是分清 RTI、PTM、HSH、光度立体、法线图这些词。

2. 再看 [02-cultural-heritage-cases.md](02-cultural-heritage-cases.md)
   先知道这些技术在碑刻、墓碑、陶器、浅浮雕上到底解决什么问题。

3. 接着看 [03-toolchain-and-datasets.md](03-toolchain-and-datasets.md)
   把 RTIViewer、RTIBuilder、OpenLIME、relight 这些工具先跑通。

4. 然后看 [06-capture-sop.md](06-capture-sop.md) 和 [09-hardware-purchase-list.md](09-hardware-purchase-list.md)
   这里对应实际采集：相机、灯、三脚架、反光球、比例尺、文件命名。

5. 如果研究对象是汉画像石和碑刻，再看 [04-han-stone-reliefs.md](04-han-stone-reliefs.md)、[05-microtrace-reproduction.md](05-microtrace-reproduction.md) 和案例目录。

6. 想继续做数据结构和 AI 辅助，再看 [10-iiml-knowledge-base.md](10-iiml-knowledge-base.md) 和 [iiml-jsonld.schema.json](iiml-jsonld.schema.json)。

## 文档目录

- [01-theory.md](01-theory.md)：RTI、PTM、HSH、RBF、光度立体、法线图等基础概念。
- [02-cultural-heritage-cases.md](02-cultural-heritage-cases.md)：文化遗产里的 RTI 和浅刻表面案例。
- [03-toolchain-and-datasets.md](03-toolchain-and-datasets.md)：工具链、公开数据和复现入口。
- [04-han-stone-reliefs.md](04-han-stone-reliefs.md)：汉画像石、拓片、中文石刻和 2.5D 浅刻资料。
- [05-microtrace-reproduction.md](05-microtrace-reproduction.md)：微痕成像、数字拓片、CHIM/IIML 和 AI 识读。
- [06-capture-sop.md](06-capture-sop.md)：面向碑刻和画像石的采集规范草稿。
- [07-software-workflow.md](07-software-workflow.md)：后续软件、数据结构和处理流程设想。
- [08-frontier-technologies.md](08-frontier-technologies.md)：前沿技术资料，先当资料库，不急着全部学完。
- [09-hardware-purchase-list.md](09-hardware-purchase-list.md)：采集设备清单。
- [10-iiml-knowledge-base.md](10-iiml-knowledge-base.md)：图像标注、知识图谱、JSON-LD 和 AI 辅助识读。
- [11-merged-project-map.md](11-merged-project-map.md)：两个项目合并后的结构说明。

## 案例

- [case-studies/stele-clarity-2026-04-27](case-studies/stele-clarity-2026-04-27)：从几张碑刻照片出发，整理了单张照片增强失败、重新采集、RTI/三维路线、汉画像石结构化和 YOLO 学习路线。

## 英文资料怎么处理

这个领域很多资料是英文的。我现在的办法不是硬啃全文，而是先做中文化处理：

1. 先翻译标题、摘要、图注和结论。
2. 把关键词做成中英文对照表。
3. 只精读和采集、流程、参数、案例有关的部分。
4. 读完一篇就写一页中文笔记：它解决什么问题、用了什么设备、我能不能照着做。

具体学习和翻译安排放在：

[tutorials/08-chinese-first-learning-route.md](tutorials/08-chinese-first-learning-route.md)

## 目前的原则

- 原始数据要保留，不要只留处理后的图。
- 每一步处理都要记参数，不然以后复查不了。
- AI 结果只能当候选，不能当定稿。
- 公开数据前要先处理 GPS、馆藏限制和版权问题。
