# RTI/PTM与汉画像石学习路线总说明

本文件是 `learning-roadmap.html` 的文字版入口。HTML页面用于浏览完整学习路线，CSV用于长期维护资料清单。

## 核心文件

- `learning-roadmap.html`：自包含HTML路线图，覆盖基础知识、论文阅读顺序、仓库工具、数据集、硬件选型和近期实验。
- `research-master-index-2026.csv`：目前为止最完整的资料总索引，含经典论文、新论文、仓库、数据集、硬件方案。
- `research-inventory-2026.csv`：上一轮新增2024-2026资料清单，保留下载状态。
- `papers/README.md`：本地PDF和论文阅读笔记索引。
- `repositories/README.md`：GitHub仓库快照和待下载仓库索引。
- `09-hardware-purchase-list.md`：详细硬件采购清单。

## 最重要的学习主线

```text
RTI/PTM基础
  -> 文化遗产案例
  -> 汉画像石/拓片/碑刻场景
  -> RelightLab工具链复现
  -> 固定光源矩阵和光度立体
  -> YOLO/SAM/IIML标注
  -> NeuralRTI/多光谱/偏振/AI线图前沿探索
```

## 第一阶段必须完成的输出

- 一份RTI/PTM/HSH/RBF/光度立体术语表。
- 一套H-RTI采集SOP。
- 一个公开样例RTI处理实验记录。
- 一个自采硬币或刻痕板实验记录。
- 一份汉画像石标注类别草案。

## 第二阶段必须完成的输出

- 16路或32路固定光源矩阵。
- `capture.json`、`lights.csv`、原始RAW和处理输出目录规范。
- 至少一个法线图、虚拟斜光图和数字拓片初稿。
- YOLO/SAM/IIML小闭环样例。

## 硬件建议

不要直接进入高预算方案。推荐路线：

1. 用低预算H-RTI包跑通采集和处理。
2. 用中预算固定光源矩阵进入微痕复现实验。
3. 等数据和流程稳定后，再扩展偏振、多光谱、3D扫描和NAS。

## 下一轮资料补齐重点

- Malzbender 2001 PTM论文和PTM格式规范PDF。
- Earl 2010 Archaeological PTM PDF。
- RelightLab 2026 Release或源码。
- OpenLIME源码和2025论文PDF。
- AnyLabeling/CVAT/Label Studio至少一个本地标注工具。
- 河南汉画像石数据库和史语所拓本典藏的字段、版权和引用规则。
