# RTI Learning 项目缺口分析 2026

本文件是在阅读当前仓库主文档、论文索引、教程、数据规范、实验模板、案例目录和工具清单后形成的下一轮完善建议。仓库已经完成了“资料收集 + 学习路线 + 初步架构”的骨架，接下来最需要把资料变成可复现数据、可运行工具和可验证实验。

## 当前已经比较扎实的部分

- RTI/PTM/H-RTI、光度立体、偏振、多光谱、Neural RTI、AI线图和图像学本体已经有学习路线。
- `papers/` 中已有 19 个本地 PDF，`papers/reading/` 中已有 2024-2026 前沿论文笔记。
- `datasets/README.md`、`experiments/README.md`、`docs/04-han-stone-ai/annotation-guidelines.md` 和 `docs/04-han-stone-ai/iiml-jsonld.schema.json` 已经形成数据治理雏形。
- `case-studies/stele-clarity-2026-04-27/` 已保留碑刻与汉画像石应用案例、来源和脚本。
- `repositories/github/NeuralRTI` 和 `external/relight` 已有部分外部代码资源，说明项目开始进入工程复现层。

## 仍未达到的关键领域

### 1. 论文 HTML 覆盖已经补齐，但还要继续升级精读深度

已统一到 `papers/reading/index.html`，并覆盖 `docs/05-validation-indexes/research-master-index-2026.csv` 中登记为 `paper` 的条目。当前目录有 38 个精读页：本地 PDF 直接嵌入，暂缺 PDF 的论文保留来源入口和中文段落组讲解。下一步不是继续堆链接，而是对三类论文做更细的逐页/逐段深读：

- PTM 源头与格式：Malzbender 2001、PTM file format、Earl 2010。
- 可复现实验论文：H-RTI、RTI增强、光度立体、DiLiGenT-Pi、定量RTI。
- 汉画像石与AI线图：Han YOLO、Relic2Contour、点云线图、ICON/IIML。
- 硬件与三维路线：Easy-to-build RTI system、Arduino 45 LED dome、汉画像石/石碑三维建模。

### 2. 第一套真正可运行的 RTI 实验还没有落地

`experiments/README.md` 已经列出实验 A-E，但目录里还没有实际实验记录。优先级应是：

1. CHI Fish Fossil 官方样例：跑通 RelightLab/RTIBuilder/RTIViewer 或 OpenLIME。
2. 硬币 H-RTI：验证反光球、手持光源、低角度重打光。
3. 刻痕板固定灯阵：输出法线图、虚拟斜光图和初版数字拓片。

没有这三组实验，项目仍停留在调研和设计层。

### 3. 固定光源矩阵和光度立体标定还缺硬件闭环

仓库已经意识到 16/32 路固定光源矩阵的重要性，但还缺：

- 灯位编号与 `lights.csv` 实例。
- 相机、对象平面、灯位坐标的测量方法。
- 过曝、阴影、环境光、灯位误差的质量检查。
- 同一对象在 8/16/32 灯下的效果对比。

这是从“看得清”走向“可生成法线/高度/数字拓片”的核心台阶。

### 4. 数据集目录有规范，但没有最小样例包

`datasets/README.md` 设计得比较完整，但还需要一个小而全的 `han-stone-demo-001` 或 `coin-rti-demo-001` 元数据样例，只提交小文件和说明，不提交大图。至少包含：

- `capture.json`
- `lights.csv`
- `processing-run.json`
- `rights.json`
- 一份实验说明
- 一份示例标注或 IIML 片段

有了这个样例，后续每次采集才不会各写各的。

### 5. IIML/JSON-LD 已有 schema，但缺一张完整样例

`docs/04-han-stone-ai/iiml-jsonld.schema.json` 和 `docs/04-han-stone-ai/10-iiml-knowledge-base.md` 已经提出方向，但还没有“从图像到解释”的完整闭环。建议选一张公开授权汉画像石图，做：

- 原图资源记录。
- RTI/增强图或拓片资源记录。
- YOLO bbox 候选。
- SAM polygon 候选。
- 人工确认对象。
- 图像志主题。
- 图像学解释。
- 证据来源和审核状态。

这一张样例会比继续扩展 schema 更有价值。

### 6. AI线图和数字拓片需要严格分层

项目已经跟踪 Relic2Contour、点云线图、扩散/LoRA 线图，但需要明确分层：

- `candidateLine`：AI候选线。
- `geometricEdge`：来自点云、法线或高度图的几何线。
- `interpretiveLine`：人工确认并带图像学含义的研究线。
- `digitalRubbing`：面向阅读/展示的数字拓片输出。

否则容易把算法噪声、视觉增强和学术释读混在一起。

### 7. 3D、RTI、IIIF/OpenLIME 发布层还没有最小演示

仓库已经记录 OpenLIME、IIIF、Annotorious、COLMAP、Meshroom、Potree、3DHOP 等方向，但还缺一个浏览器可打开的演示。最低目标是：

- 一张高分辨率图像或增强图。
- 一个标注层。
- 一个可缩放查看页面。
- 一份说明 OpenLIME、IIIF、Annotorious 各自负责什么。

后续再加 RTI 交互、3D 模型和 IIML 查询。

### 8. 外部资源和版权字段还需要落地

河南汉画像石数据库、史语所拓本典藏、Wikimedia Commons、CIT 等资源已经在索引里，但还缺访问策略：

- 可否下载。
- 是否可公开发布。
- 是否可用于训练。
- 引用方式。
- 是否需要只保存元数据和本地路径。

这部分必须在真实采集或训练前补齐，否则后续很容易出现版权和发布风险。

### 9. 工具仓库还没有“能跑/不能跑”的状态表

`docs/03-software-data/tools-evaluation-2026.md` 已有选型，但需要把工具变成运行状态：

- Relight/RelightLab：能否处理官方样例。
- OpenLIME：能否做最小网页。
- AnyLabeling/CVAT/Label Studio：至少试一个标注工具。
- COLMAP/Meshroom：至少跑一个小物体模型。
- NeuralRTI：至少跑通示例或明确依赖阻碍。

建议不要同时安装一大堆，按实验 A-E 的需要逐个验收。

## 下一轮最小闭环

```text
论文导读
  -> CHI Fish Fossil 样例处理
  -> 硬币 H-RTI 自采
  -> 固定灯阵刻痕板实验
  -> 一张公开汉画像石 YOLO/SAM/IIML 样例
  -> 一个 Web/IIIF/OpenLIME 最小展示页
```

## 建议优先级

1. 持续细化 `papers/reading/` 的人工逐页精读，先读中文解读再回到 PDF。
2. 建立 `experiments/2026-05-xx_coin_h-rti/` 第一套真实实验记录。
3. 建立 `datasets/local/coin-rti-demo-001/` 或只提交元数据样例。
4. 下载官方 CHI Fish Fossil 小样本到本地大文件区，不直接提交 Git。
5. 选一个标注工具，做 20 张公开汉画像石小样本。
6. 设计固定光源矩阵，先追求可重复，不追求高预算。

## 判断项目进入下一阶段的标准

- 能打开一页中文导读，理解每篇论文为什么重要。
- 能拿一组照片生成可查看 RTI 文件。
- 能从同一对象输出普通图、RTI增强图、法线图和实验记录。
- 能把一个 AI 候选标注写入 IIML，并说明证据来源。
- 能在浏览器中查看至少一个图像/标注/导读组合页面。

做到这里，项目就从“资料库”进入“可复现实验平台”的阶段。
