# 13 软件栈与数据架构蓝图

本文补充从采集、处理、标注、数据管理到Web发布的工程路线。目标不是立即开发完整系统，而是明确每一层应选什么工具、保存什么数据、未来如何替换。

## 总体架构

```text
采集层
  -> 数据管理层
  -> 处理计算层
  -> 标注解释层
  -> 发布展示层
  -> 知识库/训练层
```

每一层都应保留中间结果和元数据，避免“只有漂亮图，没有证据链”。

## 1. 采集层

### 设备

- 手持LED + 反光球：低成本H-RTI。
- 固定LED矩阵：光度立体和可复现微痕。
- 摄影测量照片：整体3D和局部RTI配准。
- 可选：偏振、多光谱、近红外、UV。

### 输出

- 原始RAW/JPEG/TIFF。
- `capture.json`。
- `lights.csv`。
- 灰卡/色卡/比例尺图。
- 环境和对象整体照片。

### 工具

- 相机联机拍摄软件。
- Arduino/ESP32控制脚本。
- 文件命名和校验脚本。

## 2. 数据管理层

### 本仓库保存

- 文档。
- 元数据模板。
- 小样例。
- 索引CSV。
- 代码和脚本。

### 本仓库不直接保存

- 大型RAW序列。
- 第三方数据库图片。
- 模型权重。
- 大型训练集。
- 未确认授权的馆藏图像。

### 推荐工具

- Git：文档和代码版本。
- DVC：大数据、模型和实验输出版本。
- Git LFS：少量必须跟随仓库的大文件。
- NAS/移动SSD：原始采集主存储。
- 校验：MD5/SHA256记录原始文件一致性。

## 3. 处理计算层

### RTI/PTM处理

首选：
- RelightLab。
- Relight CLI。

对照：
- RTIBuilder。
- RTIViewer。

输出：
- PTM。
- HSH/RTI。
- RBF/Relight格式。
- 法线图。
- 平均图、增强图。

### 光度立体

工具候选：
- ImageJ Photometric Stereo Tools。
- `near_ps`。
- `visiont3lab/photometric_stereo`。
- Meshroom/AliceVision Photometric Stereo节点。

输出：
- 法线图。
- 反照率图。
- 高度图。
- 拟合误差图。

### 3D重建

工具候选：
- COLMAP。
- Meshroom/AliceVision。
- Metashape（商业，可作为对照）。
- CloudCompare。
- MeshLab。

用途：
- 整体对象建模。
- 正射图生成。
- 局部RTI区域配准。
- 点云/网格线图提取。

### 3D Web展示

工具候选：
- 3DHOP。
- Potree。
- Universal Viewer。
- Sketchfab（外部平台，注意版权）。

用途：
- 高分辨率3D模型展示。
- 点云展示。
- 博物馆展示和教学。

## 4. 标注解释层

### 快速个人标注

推荐：
- AnyLabeling。

原因：
- 桌面使用简单。
- 支持YOLOv8。
- 支持SAM、SAM2、SAM3、MobileSAM。
- 适合快速制作小样本。

### 正式协作标注

候选：
- CVAT。
- Label Studio。

选择建议：
- 如果目标是CV/YOLO/COCO数据集，优先CVAT。
- 如果同时管理图像、文本、释读、审核流程，评估Label Studio。

### Web标注原型

候选：
- Annotorious。
- OpenSeadragon。
- Mirador。
- IIIF Web Annotation。

用途：
- 大图和IIIF图像标注。
- 与IIML JSON-LD互操作。
- 浏览器内展示研究标注。

## 5. 发布展示层

### 二维/RTI发布

推荐：
- OpenLIME。
- IIIF Image API。
- DeepZoom。

能力：
- 高分辨率图像。
- RTI重打光。
- 多图层叠加。
- 标注和测量。
- 多光谱/BRDF/神经重光照扩展。

### 三维发布

推荐：
- 3DHOP：文化遗产高分辨率3D模型。
- Potree：大型点云。
- Universal Viewer：IIIF和多媒体展示。

## 6. 知识库/训练层

### 文件格式

- IIML JSON-LD：本项目核心交换格式。
- COCO/YOLO：训练数据格式。
- Web Annotation：Web互操作。
- RDF/JSON-LD：知识图谱。

### 后端候选

第一阶段：
- 文件系统 + JSON。
- SQLite。

第二阶段：
- PostgreSQL。
- FastAPI。
- 对象存储/NAS。

第三阶段：
- RDF triplestore。
- Neo4j。
- Wikibase。

## 7. 最小可行系统

第一版系统不需要复杂后端，只要能完成：

```text
导入增强图
  -> 创建多边形标注
  -> 绑定词表项
  -> 标记证据资源
  -> 导出IIML JSON-LD
  -> 用JSON Schema校验
```

推荐技术：
- 前端：OpenSeadragon + Annotorious。
- 数据：JSON-LD文件。
- 校验：`docs/04-han-stone-ai/iiml-jsonld.schema.json`。
- 标注预处理：AnyLabeling导出，再转换。

## 8. 中期系统

```text
项目管理
  -> 数据导入
  -> Relight/光度立体处理调用
  -> 输出资源版本链
  -> 标注审核
  -> IIIF/OpenLIME发布
  -> YOLO训练数据导出
```

推荐技术：
- Python CLI。
- FastAPI。
- SQLite/PostgreSQL。
- OpenLIME。
- CVAT或Label Studio。

## 9. 长期系统

```text
多馆藏资源
  -> IIIF聚合
  -> RTI/3D/多光谱多模态
  -> 图像学知识图谱
  -> 纹样检索
  -> AI辅助释读
  -> 可公开发布研究包
```

关键能力：
- 多版本资源管理。
- 坐标转换。
- 词表映射。
- 多研究者分歧管理。
- 模型训练和评估记录。

## 10. 工具优先级

### 立即学习

- RelightLab。
- RTIViewer。
- OpenLIME。
- AnyLabeling。
- COLMAP或Meshroom。

### 中期学习

- CVAT。
- ImageJ Photometric Stereo Tools。
- CloudCompare。
- MeshLab。
- DVC。

### 长期学习

- 3DHOP。
- Potree。
- Mirador。
- Neo4j/RDF。
- NeuralRTI/DisK-NeuralRTI。

## 11. 风险

- 工具太多导致分散，应以实验闭环驱动工具选择。
- AI输出容易生成伪线和误标，必须人工审核。
- 3D模型和RTI局部区域配准会产生坐标误差。
- 大数据不能直接进Git，必须建立外部存储策略。
- 馆藏图片版权和文物敏感信息必须优先处理。

## 12. 下一步

- [ ] 为`datasets/README.md`补一个最小样例目录。
- [ ] 写`tools-evaluation.md`，对Relight/OpenLIME/CVAT/AnyLabeling做评分。
- [ ] 写一个IIML最小JSON样例。
- [ ] 试运行AnyLabeling，导出YOLO/SAM样例。
- [ ] 试运行COLMAP或Meshroom，生成一个小型3D模型。
