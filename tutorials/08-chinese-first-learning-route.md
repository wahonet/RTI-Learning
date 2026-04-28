# 英文资料学习顺序

RTI、photometric stereo、IIIF、CIDOC CRM、YOLO 等资料以英文为主。学习时先处理关键内容，再进入全文阅读和复现。

## 基本顺序

一篇英文论文或教程按以下顺序处理：

1. 标题。
2. 摘要。
3. 图、表格、流程图。
4. 结论。
5. 设备、软件、参数、数据格式。
6. 关键词中英文对照。
7. 中文摘要。

暂时读不懂的资料，先记录三项：

- 研究对象。
- 使用方法。
- 与采集、处理或结构化的关系。

## 术语表

### RTI 和成像

| English | 中文 |
| --- | --- |
| Reflectance Transformation Imaging, RTI | 反射变换成像 |
| raking light | 斜光 |
| highlight capture | 高光球采集 |
| normal map | 法线图 |
| photometric stereo | 光度立体 |
| relighting | 重新打光 |
| digital rubbing | 数字拓片 |

### 三维采集

| English | 中文 |
| --- | --- |
| photogrammetry | 摄影测量 |
| SfM | 运动恢复结构 |
| MVS | 多视图立体 |
| point cloud | 点云 |
| mesh | 网格模型 |
| texture | 纹理 |
| orthophoto | 正射影像 |
| structured light | 结构光扫描 |
| laser scanning | 激光扫描 |

### 图像结构化和 AI

| English | 中文 |
| --- | --- |
| object detection | 目标检测 |
| bounding box, bbox | 矩形框 |
| segmentation | 分割 |
| annotation | 标注 |
| label | 标签 |
| training set | 训练集 |
| validation set | 验证集 |
| test set | 测试集 |
| precision | 精确率 |
| recall | 召回率 |
| knowledge graph | 知识图谱 |
| ontology | 本体 |

## 6 个月学习路线

### 第 1 月：RTI 和斜光

任务：

- 阅读 RTI 入门资料。
- 翻译 RTI 采集指南中的关键步骤。
- 使用硬币、石头或砖进行 8-16 方向斜光拍摄。

产出：

- RTI 术语表。
- 一组斜光实验照片。
- 实验记录，包括光源方向和细节变化。

### 第 2 月：可复核采集

任务：

- 学习曝光、白平衡、RAW、三脚架、比例尺和编号。
- 制作采集表。
- 对碑刻或画像石局部拍摄多方向光。

产出：

- 采集 SOP 草稿。
- 一组可复查的采集数据。

### 第 3 月：摄影测量和三维基础

任务：

- 学习 Meshroom 或 Metashape。
- 使用 80-150 张照片重建一个小物件。
- 区分点云、网格、纹理和正射图。

产出：

- 小型三维模型。
- 重建失败原因记录。

### 第 4 月：数字拓片和三维后处理

任务：

- 学习 CloudCompare、MeshLab、GigaMesh 的基本查看功能。
- 尝试法线图、曲率图、环境遮蔽图。
- 比较普通照片、斜光图、RTI 图和三维渲染图。

产出：

- 多种图像结果对比表。

### 第 5 月：汉画像石结构化

任务：

- 建立小型对象词表：人物、马、车、乐器、建筑、日月、榜题。
- 使用 VIA、Label Studio 或 CVAT 标注 50-100 张图。
- 记录场景、对象和关系。

产出：

- CSV/JSON 标注样例。
- 图像题材词表草稿。

### 第 6 月：YOLO 和 AI 辅助

任务：

- 运行 Ultralytics YOLO。
- 训练少量类别，如人、马、车、榜题。
- 分析漏检和误检。

产出：

- 小型检测模型。
- 错误分析。
- “图像 -> 对象 -> 关系 -> 题材”的结构化样例。

## 每周安排

每周 6 小时：

- 2 小时翻译和阅读。
- 2 小时软件操作。
- 1 小时实拍或整理图片。
- 1 小时写记录。

每周 10 小时：

- 3 小时阅读和翻译。
- 3 小时软件操作。
- 2 小时采集实验。
- 2 小时整理数据和记录。

## 翻译范围

优先翻译：

- 摘要
- 结论
- 方法流程
- 设备清单
- 参数表
- 图注
- 数据格式说明

中文笔记格式：

```text
资料名称：
研究对象：
方法：
设备和软件：
流程：
可借鉴内容：
未理解问题：
```
