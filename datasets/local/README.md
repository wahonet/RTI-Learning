# 本地自建数据目录

此目录用于本机保存自采RTI、光度立体、3D和标注数据。大图、RAW、处理输出和训练集默认不提交到Git。

建议每个数据集建立独立目录，例如：

```text
han-stone-demo-001/
  capture.json
  raw/
  metadata/
  processed/
  annotations/
  notes/
```

只有元数据模板、小样例和说明文档可以提交。
