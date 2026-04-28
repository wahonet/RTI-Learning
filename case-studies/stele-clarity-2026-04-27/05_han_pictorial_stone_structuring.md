# 汉画像石图像结构化：研究领域与落地方案

整理日期：2026-04-27。

## 先给结论

汉画像石图像结构化，不能简单理解为“给图片打几个标签”。更合适的目标是把一块画像石拆成：

1. **文物层**：哪块石、出土哪里、年代、材质、尺寸、收藏单位、墓葬空间位置。
2. **图像层**：照片、拓片、线描、3D、RTI、数字拓片之间的对应关系。
3. **版面层**：边框、榜题、分栏、分格、上下层、中心图像、装饰带。
4. **对象层**：人物、神灵、动物、车马、乐器、建筑、兵器、日月、云气、树木等。
5. **关系层**：谁骑什么、谁持什么、谁朝向谁、谁在谁上方、哪几个人属于同一场景。
6. **题材层**：伏羲女娲、西王母、东王公、车马出行、乐舞百戏、狩猎、庖厨、历史故事、孝子故事、升仙图像等。
7. **解释层**：研究者释读、争议说法、平行图像、参考文献、置信度。
8. **AI 层**：检测框、分割 mask、视觉特征、OCR/榜题识别、模型候选、人工确认状态。

一句话：**汉画像石结构化的核心是“图像证据 + 空间位置 + 图像学语义 + 文献解释 + 不确定性”同时保存。**

## 相关研究领域

### 1. 汉画像石数字化保护与 3D 建模

这类研究关注采集、保存、展示和复原。比如 2023 年关于南阳地区汉画像石的 3D 数字建模论文，提出从三维扫描、数据采集处理、3D 建模、可视化到信息利用的工作流。它强调画像石虽然是雕刻，但主要信息集中在表面线条和浅浮雕上，3D 点云能记录纹饰、文字、深度、尺寸等细节。

对结构化的启发：

- 不应只保存一张平面图。
- 每个对象最好能绑定到 2D 坐标和 3D 表面位置。
- 如果有 3D，就可以记录刻线深度、浮雕高度、损伤和修复状态。

### 2. 汉画像石目标检测 / 深度学习识别

2024 年 npj Heritage Science 有一篇直接相关论文：**Human figure detection in Han portrait stone images via enhanced YOLO-v5**。

它的价值在于：

- 明确把汉画像石中的人物识别转成目标检测任务。
- 指出画像石的难点：复杂背景、密集目标、尺度变化大、人物与纹饰边界不清。
- 数据集人工标注，包含训练集 123 张、验证集 80 张、测试集 82 张。
- 目标类别包括伏羲女娲、乐舞场景等。
- 模型在 YOLOv5 上加入 SPD-Conv、Coordinate Attention、DIoU NMS、Alpha-IoU Loss，用来改善小目标、密集目标和背景干扰。

对结构化的启发：

- AI 可以先做“对象候选”，不要直接做整图解释。
- 最先适合训练的类别是高频、形态相对稳定的对象：人、马、车、乐器、建筑、日月、鸟兽、伏羲女娲、西王母等。
- 数据集很小也能开始，但必须人工标注，而且要有专家校验。

### 3. 图像学、题材学、符号学研究

汉画像石本来就是图像学研究对象。现有文科研究常见主题包括：

- 地域：徐州、南阳、山东、陕北、四川等。
- 题材：神仙、历史故事、车马出行、乐舞百戏、庖厨宴饮、狩猎、祥瑞动物、墓主生活。
- 形制：墓门、墓室壁面、祠堂、阙、棺椁构件、横额、立柱、门楣。
- 图像语义：升仙、辟邪、孝义、忠烈、礼制、墓葬仪式、社会生活。

对结构化的启发：

- 题材标签不能只用现代物体名，还要用汉画像石研究的传统术语。
- 同一个对象可能有多层意义，比如“鸟”可能只是动物，也可能是祥瑞、仙界、日月神话的一部分。
- 要允许“一图多解”和“不确定”。

### 4. 文化遗产知识图谱

文化遗产管理里已经有很多知识图谱研究。知识图谱适合解决“馆藏信息、考古报告、图片、研究文献、人物地点、图像主题”彼此割裂的问题。

可借鉴标准：

- **CIDOC CRM**：博物馆与文化遗产领域的高层本体，适合描述文物、地点、事件、制作、发现、收藏、测量、资料来源。
- **CRMdig**：CIDOC CRM 的数字化扩展，可描述数字对象、采集活动、处理流程和衍生文件。
- **LIDO**：博物馆对象数据交换。
- **Linked Art**：面向艺术品开放数据的 JSON-LD 模型。
- **Wikidata**：可以借用通用实体、地名、人物、概念 URI。

对结构化的启发：

- 画像石项目不必重新发明全部元数据标准。
- 可用 CIDOC CRM 管“文物/地点/事件/收藏”，用自定义汉画像石本体管“图像题材/对象/关系”。

### 5. IIIF 与图像标注

IIIF 是文化遗产图像发布和标注的重要标准。它把高清图像、缩放浏览、局部区域标注、Manifest 元数据、Web Annotation 结合起来。

对结构化的启发：

- 画像石的每个对象、场景、题记都可以作为 IIIF annotation。
- 标注结果可以绑定到图像坐标区域，而不是只存文字描述。
- 适合多人协作、教学、远程校读和长期发布。

### 6. Iconclass 与图像题材分类

Iconclass 是西方艺术史常用的图像题材分类系统。它不适合直接套到汉画像石上，但方法值得学：它把题材、母题、人物、动作、象征意义组织成可检索的层级分类。

对结构化的启发：

- 可以建立一个“中国汉画像石 Iconclass-like 词表”。
- 词表要同时支持宽泛标签和细分标签：例如“神话图像 > 伏羲女娲 > 人首蛇身 > 执规矩”。

### 7. Scene Graph / 场景图

计算机视觉中的 scene graph 把图像表示成：

```text
对象 A --关系--> 对象 B
```

例如：

```text
人物1 --骑乘--> 马1
人物1 --手持--> 戟1
马1 --牵引--> 车1
车1 --属于场景--> 车马出行
```

对汉画像石非常有用，因为它不只记录“有什么”，还记录“谁和谁发生了什么关系”。

### 8. 多模态检索与 RAG

最终可将图像、释文、文献、题材标签、坐标框、3D 数据放入同一知识库，用于支持 AI 问答：

- 哪些画像石出现了“伏羲女娲 + 日月 + 执规矩”？
- 徐州和南阳的车马出行图有什么差异？
- 哪些乐舞图中出现建鼓、长袖舞、伴奏者？
- 某个损坏图像可能对应哪些平行图像？

这需要图像结构化先做好，AI/RAG 才有可靠依据。

## 推荐的结构化层级

### A. 文物与来源

字段示例：

- `artifact_id`
- `name`
- `artifact_type`：画像石、画像砖、墓门、门楣、墓室壁石、祠堂石刻等
- `dynasty`
- `date_range`
- `excavation_place`
- `current_location`
- `material`
- `dimensions`
- `carving_technique`
- `condition`
- `bibliography`

### B. 数字资源

- `image_id`
- `resource_type`：photo、rubbing、line_drawing、3d_model、rti、digital_rubbing
- `capture_method`
- `resolution`
- `iiif_manifest`
- `file_path`
- `derived_from`
- `processing_notes`

### C. 版面结构

- `panel`
- `register`
- `frame`
- `scene`
- `inscription_area`
- `ornamental_band`
- `damage_area`

每个结构单元都应有：

- `bbox` 或 `polygon`
- `parent_id`
- `reading_or_viewing_order`
- `confidence`

### D. 对象实体

建议先从 30-50 个常用类开始，而不是一上来做几百类。

第一批对象词表：

- 人物：人、侍者、舞者、乐师、骑者、墓主、神人
- 神话人物：伏羲、女娲、西王母、东王公、羽人、仙人
- 动物：马、龙、虎、鸟、凤、鹿、犬、鱼
- 车马：车、马、御者、车轮、轭、舆
- 乐舞：建鼓、钟、磬、琴瑟、吹奏者、舞者
- 建筑：阙、门、楼阁、柱、帷帐
- 器物：鼎、壶、案、杯、兵器、规、矩
- 天象：日、月、星、云气
- 装饰：几何纹、连弧纹、菱格纹、边框
- 文字：榜题、题记、铭文

### E. 关系

关系词表要少而稳定：

- 空间关系：`left_of`、`right_of`、`above`、`below`、`inside`、`overlaps`
- 动作关系：`rides`、`holds`、`plays`、`dances`、`hunts`、`drives`、`offers`
- 组合关系：`part_of_scene`、`part_of_vehicle`、`part_of_register`
- 朝向关系：`faces`、`faces_left`、`faces_right`
- 图像学关系：`identified_as`、`possibly_identified_as`、`parallel_to`

### F. 题材与解释

- `theme_primary`
- `theme_secondary`
- `iconographic_motifs`
- `interpretation`
- `alternative_interpretations`
- `evidence`
- `bibliography`
- `certainty`

## 示例 JSON

```json
{
  "artifact_id": "xuzhou_hhs_001",
  "name": "车马出行画像石",
  "artifact_type": "画像石",
  "dynasty": "东汉",
  "current_location": "徐州博物馆",
  "resources": [
    {
      "image_id": "xuzhou_hhs_001_photo_01",
      "resource_type": "photo",
      "file_path": "images/xuzhou_hhs_001.jpg",
      "iiif_manifest": ""
    }
  ],
  "regions": [
    {
      "region_id": "scene_01",
      "type": "scene",
      "polygon": [[120, 80], [900, 80], [900, 420], [120, 420]],
      "theme_primary": "车马出行",
      "confidence": 0.86
    }
  ],
  "objects": [
    {
      "object_id": "horse_01",
      "class": "马",
      "bbox": [230, 210, 150, 80],
      "part_of": "scene_01",
      "source": "human_annotation",
      "confidence": 0.95
    },
    {
      "object_id": "rider_01",
      "class": "骑者",
      "bbox": [250, 150, 80, 110],
      "part_of": "scene_01",
      "source": "human_annotation",
      "confidence": 0.9
    }
  ],
  "relations": [
    {
      "subject": "rider_01",
      "predicate": "rides",
      "object": "horse_01",
      "confidence": 0.92
    }
  ],
  "interpretations": [
    {
      "target": "scene_01",
      "text": "该区域可释为车马出行场景。",
      "certainty": "probable",
      "bibliography": []
    }
  ]
}
```

## 落地路线

### 第 1 步：不要先训练模型，先建词表

先选 3-5 个高频题材：

- 伏羲女娲
- 西王母/东王公
- 车马出行
- 乐舞百戏
- 庖厨宴饮

每个题材列：

- 常见构成元素
- 典型构图
- 易混对象
- 关键词
- 参考图例
- 争议点

### 第 2 步：建最小标注规范

先做三层标注：

1. 整体题材标签。
2. 场景/分格 polygon。
3. 对象 bbox 或 polygon。

暂时不要强求每根线都分割出来，否则工作量会炸。

### 第 3 步：用工具标注 100-300 张图

推荐工具：

- **VGG Image Annotator (VIA)**：最轻，本地一个 HTML 就能用，适合文科团队试标。
- **Label Studio**：适合多人协作、图像+文本、多模态标注。
- **CVAT**：适合严肃计算机视觉训练，支持框、多边形、分割、质量控制。
- **IIIF + Web Annotation**：适合长期发布和学术标注。

### 第 4 步：训练对象检测模型

第一批可以训练：

- 人物/动物/车马/乐器/建筑/日月/文字区
- 伏羲女娲、西王母、乐舞、车马出行等高频题材

模型不必从头写：

- YOLOv8/YOLOv9/YOLOv10/YOLOv11 系列适合快速检测。
- Mask R-CNN / SAM-assisted annotation 适合对象轮廓。
- Grounding DINO + SAM 可做“文本提示 + 分割”的半自动标注，但汉画像石领域词汇需要人工校验。

### 第 5 步：建立知识图谱

结构建议：

```text
文物 -> 资源 -> 区域 -> 对象 -> 关系 -> 题材 -> 解释 -> 文献
```

存储可以从简单到复杂：

- 初期：CSV/JSON。
- 中期：SQLite + JSON 文件。
- 后期：Neo4j / RDF triplestore / PostgreSQL。

### 第 6 步：接 AI 问答和检索

AI 最适合做：

- 根据结构化数据生成说明文字。
- 根据题材、对象、关系做检索。
- 找平行图像。
- 辅助提出可能解释。

AI 不适合直接做最终释读。最终仍然需要专家确认。

## 汉画像石结构化的难点

1. **对象边界不清**：线刻、浅浮雕、拓片噪声、残损会让框选很难。
2. **同一对象形态变化大**：伏羲女娲、西王母、舞者、车马都存在地域与时代差异。
3. **题材不是简单物体分类**：看到“鸟”不等于理解它在仙界/祥瑞/日月神话中的意义。
4. **图像叙事有空间顺序**：上下层、左右分格、墓室方位都会影响解释。
5. **公开数据集不足**：现有研究多用自建小数据集，难以直接复用。
6. **需要保留不确定性**：结构化不是把争议抹平，而是把证据、解释和置信度保存下来。

## 最小可行项目

可发表、可扩展的小项目可以从以下范围开始：

题目：**汉画像石车马出行图像结构化标注与检索试验**

范围：

- 选 100 张车马出行相关图像。
- 每张图记录文物元数据、来源、地域、年代。
- 标注场景区域、人物、马、车、建筑、榜题。
- 记录关系：人骑马、人驾车、马牵车、人物位于车内。
- 做一个 JSON/CSV 数据集。
- 训练一个轻量 YOLO 检测器。
- 做一个检索页面：按“有车+两马+执兵器人物”等条件查图。

为什么选这个：

- 题材高频。
- 对象相对明确。
- 对汉代交通、礼制、墓葬图像研究都有意义。
- 比直接做“全部汉画像石自动理解”现实得多。

## 推荐阅读和工具

### 论文与项目

- Human figure detection in Han portrait stone images via enhanced YOLO-v5。
- 3D Digital Modeling as a Sustainable Conservation and Revitalization Path for the Cultural Heritage of Han Dynasty Stone Reliefs。
- Tomb Rituals in Han Dynasty Pictorial Stone Reliefs: Depictions of Historical Figures。
- Using knowledge graphs and deep learning algorithms to enhance digital cultural heritage management。
- IICONGRAPH: improved Iconographic and Iconological Statements in Knowledge Graphs。
- Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations。

### 标准

- CIDOC CRM。
- CRMdig。
- IIIF Presentation API / Image API / Web Annotation。
- LIDO。
- Linked Art。
- Iconclass。

### 工具

- VIA：轻量本地标注。
- Label Studio：多人和多模态标注。
- CVAT：计算机视觉数据集标注。
- OpenLIME：高分辨图像、RTI、多层图像查看。
- Recogito/IIIF 标注工具：学术图像标注。
- Neo4j：知识图谱原型。
- QGIS：如果要把出土地理位置和区域传播结合起来。
