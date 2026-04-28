# RTI-Learning 与 relics-align2 合并说明

整理日期：2026-04-28。

## 共同点

两个项目的核心问题是一致的：如何把石质文物表面的浅刻、低浮雕、风化纹理、榜题和图像内容稳定采集下来，并进一步转化为可复核、可检索、可被 AI 辅助处理的数据。

共同主题包括：

- RTI、多方向斜光、光度立体和三维表面信息采集。
- 碑刻、墓碑、汉画像石、浅浮雕等低对比石质对象。
- 数字拓片、法线图、曲率图、环境遮蔽等细节增强方式。
- 图像、3D、释文、标注、题材和文献之间的结构化关联。
- AI 只做候选和辅助，最终判断需要人工校读和图像学/碑刻学依据。

## 差异

`RTI-Learning` 原来更像基础知识库：

- 理论：RTI、PTM、HSH、RBF、photometric stereo。
- 工具：RTIViewer、RTIBuilder、OpenLIME、RelightLab 等。
- 文献：论文 PDF、教程、硬件清单、采集 SOP。
- 数据模型：IIML / JSON-LD 工作草案。

`relics-align2` 更像应用案例：

- 从实际碑刻照片后期增强失败出发。
- 转向重新采集、RTI、三维扫描、数字拓片。
- 扩展到汉画像石图像结构化、YOLO 检测、知识图谱和学习路线。
- 包含一个 OpenCV 样例脚本和本地实验输出。

## 合并策略

合并后采用“主干知识库 + 应用案例”的结构：

```text
RTI-Learning/
  01-10 主线学习文档
  11-merged-project-map.md
  iiml-jsonld.schema.json
  papers/
  tutorials/
  case-studies/
    stele-clarity-2026-04-27/
      01-06 研究和学习文档
      sources.csv
      acquisition_sources.csv
      han_pictorial_stone_structuring_sources.csv
      tools/stele_enhance.py
      inputs/README.md
      outputs/README.md
```

原始照片和生成图保留在本地，不纳入 GitHub 跟踪。原因：

- 原始照片带有经纬度水印，公开前应做脱敏判断。
- 输出图是可重复生成的中间产物，不应膨胀 Git 仓库。
- 仓库的主要价值是学习路线、研究资料、代码和可复核流程。

## 合并后的主线

1. 用 `01-08` 理解 RTI/photometric stereo/3D/多光谱等采集与增强技术。
2. 用 `06-capture-sop.md` 和 `09-hardware-purchase-list.md` 规划现场采集。
3. 用 `case-studies/stele-clarity-2026-04-27` 理解真实碑刻照片为什么单张后期增强有限，以及如何转向多光照和三维采集。
4. 用 `05_han_pictorial_stone_structuring.md` 和 `06_yolo_learning_route.md` 进入汉画像石结构化和目标检测。
5. 用 `10-iiml-knowledge-base.md` 和 `iiml-jsonld.schema.json` 把对象、关系、释文、题材、文献和 AI 候选组织成机器可读数据。

## 后续建议

- 建一个真实采集案例：每块碑保存整体照、近景多光照、RTI/3D 结果、数字拓片、人工释读表。
- 建一个汉画像石最小标注集：先从车马出行、乐舞百戏、伏羲女娲等高频题材开始。
- 不急于追求端到端 AI，先确保采集、标注、数据结构和人工校读流程稳定。
- 公开数据前单独处理版权、GPS、馆藏限制和文物点位保护问题。
