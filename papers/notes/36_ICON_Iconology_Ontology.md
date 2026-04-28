# ICON Ontology and iconographical/iconological statements

相关资料：

- [ICON: An Ontology for Comprehensive Artistic Interpretations, ACM JOCCH 2023](https://dl.acm.org/doi/10.1145/3594724)
- [Improving Retrieval and Expression of Iconographical and Iconological Semantic Statements, 2024](https://link.springer.com/chapter/10.1007/978-3-031-72437-4_10)
- [ArtDL iconography classification dataset](https://re.public.polimi.it/retrieve/7cd13dc6-2605-4310-acda-7faff82c062d/arxiv_2010.11697v3.pdf)

## 资料在做什么

ICON Ontology面向艺术品图像学和图像解释建模。它参考Panofsky三层解释理论，把艺术品的前图像志、图像志、图像学解释拆分成可表达、可检索、可链接的数据结构。2024年的扩展进一步改善解释者、主体特征、不同解释层级和检索表达。

ArtDL则从AI角度研究图像志分类，构建带Iconclass标签的圣徒图像数据集，并用CNN做图像志类别识别。

## 对汉画像石形相学/IIML的价值

汉画像石不能只做“目标检测框”。图像学研究需要表达：

- 画面中有什么元素。
- 元素之间的空间关系。
- 元素之间的叙事关系。
- 某一元素为何被解释为某个神话、仪式或图像主题。
- 不同研究者的不同解释和证据来源。

ICON Ontology提示本项目在IIML中至少要分层：

- 几何层：点、线、框、多边形。
- 前图像层：人物、马、车、树、门阙、神兽等可见对象。
- 图像志层：伏羲女娲、乐舞百戏、车马出行、升仙等主题。
- 图像学层：宇宙观、墓葬礼仪、祥瑞、身份表达等解释。

## 与YOLO/SAM标注的关系

YOLO只负责粗定位，SAM可生成候选多边形，它们都不能替代图像学解释。本项目应把AI结果作为IIML中的候选几何和候选标签，人工确认后再进入正式知识库。

推荐字段：

- `interpretationLevel`：pre-iconographical/iconographical/iconological。
- `evidenceResource`：依据的原图、RTI增强图、拓片、线图或论文。
- `confidence`：置信度。
- `reviewStatus`：candidate/reviewed/rejected。
- `agent`：人工研究者或AI模型。
- `relation`：contains、partOf、faces、rides、holds、above等。

## 局限

- ICON主要面向西方艺术史，需要映射到中国汉画像石术语。
- Iconclass不能直接覆盖汉代图像系统。
- 形相学还需要本土学术概念和汉画总录类资料补充。

## 后续任务

- 建立汉画像石本地词表，并逐步映射Wikidata、Getty AAT、Iconclass中可对应的概念。
- 在`iiml-jsonld.schema.json`中增加解释层级和证据字段。
- 选一张汉画像石，做从YOLO框、SAM多边形到图像学关系的完整标注样例。
