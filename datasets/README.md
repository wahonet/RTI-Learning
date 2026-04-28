# 数据集与资源管理规范

本目录用于记录数据集规范、外部数据入口和自建数据目录结构。原则上不把大体量原始照片、第三方数据集、馆藏图像和训练数据直接提交到Git；仓库只保存索引、元数据模板、下载说明和小样例。

外部数据源清单见 `external-index.csv`。

## 数据类型

### 1. 原始采集数据

包括：
- RAW照片。
- JPEG/TIFF导出。
- 多光照照片序列。
- 灰卡、色卡、比例尺、反光球照片。
- 环境照片和对象整体照片。

要求：
- 原始文件只读保存，不覆盖。
- 每组数据必须有`capture.json`。
- 固定灯阵数据必须有`lights.csv`。
- 文件名应稳定、可排序、可映射光源编号。

### 2. 处理数据

包括：
- 去畸变/裁剪/白平衡后的图像。
- RTI/PTM/HSH/RBF/Relight输出。
- 法线图、反照率图、高度图。
- 虚拟掠射光图、增强图、数字拓片、线图。

要求：
- 每个处理结果必须有`processing-run.json`。
- 不覆盖旧版本，按处理版本保存。
- 记录软件、版本、参数、输入资源和输出资源。

### 3. 标注数据

包括：
- YOLO bbox。
- COCO segmentation。
- LabelMe/Label Studio/CVAT导出。
- SAM候选mask。
- IIML JSON-LD。
- 人工审核结果。

要求：
- 标注必须绑定具体图像版本。
- AI标注默认是候选，不是最终释读。
- 保留标注者、模型、置信度、审核状态和时间。

### 4. 外部数据

包括：
- CHI Fish Fossil Sample。
- VAT楔形文字RTI数据。
- DiLiGenT-Pi光度立体数据。
- Antikythera PTM数据。
- 河南汉画像石图像数据库。
- 史语所汉代石刻画像拓本典藏。
- Wikimedia Commons开放图片。

要求：
- 不批量抓取受版权限制的数据。
- 记录访问日期、URL、授权、引用方式。
- 如需训练，只保存本地派生索引，不把第三方大图提交到Git。

## 推荐目录结构

```text
datasets/
  README.md
  external-index.csv
  samples/
    README.md
  local/
    han-stone-demo-001/
      capture.json
      raw/
      metadata/
        lights.csv
        camera.json
        rights.json
      processed/
        relight/
        normals/
        enhanced/
        lineart/
      annotations/
        yolo/
        coco/
        iiml/
      notes/
        experiment.md
```

`local/`和大图数据后续应加入`.gitignore`，只提交README和小型元数据样例。

## `capture.json`模板

```json
{
  "datasetId": "han-stone-demo-001",
  "objectId": "object-001",
  "objectName": "",
  "objectType": "han_stone_relief",
  "captureDate": "2026-04-29",
  "operator": "",
  "location": "",
  "camera": {
    "model": "",
    "lens": "",
    "focalLengthMm": null,
    "aperture": "",
    "shutter": "",
    "iso": null,
    "whiteBalance": "",
    "format": "RAW+JPEG"
  },
  "lighting": {
    "method": "highlight_rti",
    "lightCount": null,
    "lightType": "",
    "colorTemperatureK": null,
    "hasReflectiveSphere": true,
    "hasFixedLightRig": false
  },
  "scale": {
    "hasScaleBar": true,
    "unit": "mm"
  },
  "rights": {
    "owner": "",
    "license": "",
    "publicRelease": false,
    "notes": ""
  },
  "notes": ""
}
```

## `processing-run.json`模板

```json
{
  "processingRunId": "run-001",
  "inputDatasetId": "han-stone-demo-001",
  "software": {
    "name": "RelightLab",
    "version": "",
    "url": "https://github.com/cnr-isti-vclab/relight"
  },
  "method": "hsh",
  "parameters": {
    "crop": null,
    "basis": "hsh",
    "normalExport": true
  },
  "inputs": [],
  "outputs": [],
  "createdAt": "2026-04-29",
  "notes": ""
}
```

## 外部资源索引字段

建议`external-index.csv`使用以下字段：

```text
id,name,type,url,license,access_date,local_status,notes
```

状态建议：
- `tracked`：已记录入口。
- `downloaded_local`：已下载到本地但不进Git。
- `sample_committed`：只提交小样例或元数据。
- `restricted`：有版权或访问限制。
- `needs_review`：需要确认授权。

## 数据治理原则

- Git保存代码、文档、索引和小型元数据。
- 大图、RAW、模型权重、训练集放本地硬盘、NAS或DVC/对象存储。
- 外部馆藏图片必须尊重授权，不把不确定版权的数据公开推送。
- 任何AI训练集都要能追溯到原图、标注者、标注版本和许可状态。
- 公开发布前清理GPS、水印、个人信息和馆藏敏感信息。

## 后续任务

- [ ] 建立`external-index.csv`。
- [ ] 建立一个最小`han-stone-demo-001`元数据样例。
- [ ] 确定是否使用DVC管理本地大数据。
- [ ] 建立YOLO/COCO/IIML格式转换脚本。
- [ ] 给每个数据集补版权和引用说明。
