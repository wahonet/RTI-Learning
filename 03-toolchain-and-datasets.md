# 03 工具链与公开数据集复现

## 学习目标

用公开工具和公开数据集跑通RTI处理闭环，掌握从照片序列到RTI/PTM/HSH/RBF、法线图、增强图和Web查看器的流程。这个阶段是后续微痕复现和软件开发的技术基线。

## 工具链优先级

### Relight / RelightLab

链接：[cnr-isti-vclab/relight](https://github.com/cnr-isti-vclab/relight)

定位：
- 当前优先工具。
- 支持GUI和CLI。
- 支持RTI创建、法线图、PTM、HSH、RBF、Web发布。
- 与OpenLIME生态连接更自然。

需要评估：
- Windows可用性。
- CLI参数完整性。
- 输入目录结构和光照方向文件格式。
- 法线图导出质量。
- 高分辨率和批处理能力。

实验记录模板：

```markdown
## Relight实验记录

- 数据集：
- 照片数量：
- 输入格式：
- 光照方向来源：
- 输出格式：
- 处理时间：
- 输出大小：
- 观察到的问题：
- 对微痕增强的价值：
```

### RTIViewer

链接：[Cultural Heritage Imaging: RTIViewer](https://culturalheritageimaging.org/What_We_Offer/Downloads/View/)

定位：
- 经典查看器。
- 适合学习RTI查看模式和增强模式。
- 用作Relight/OpenLIME结果的效果对照。

需要评估：
- PTM/HSH/RTI兼容性。
- 增强模式：diffuse gain、specular enhancement、normal visualization。
- 书签、注释和研究记录能力。

### RTIBuilder

链接：[Cultural Heritage Imaging: RTIBuilder / Processing](https://culturalheritageimaging.org/What_We_Offer/Downloads/Process/)

定位：
- 传统流程参考。
- 适合学习highlight method。
- 不作为长期主工具，因为官方已说明它较旧，现代系统建议关注RelightLab。

需要评估：
- 处理流程和术语。
- 高光球检测逻辑。
- PTM/HSH输出差异。
- 对现代操作系统的限制。

### OpenLIME

链接：[OpenLIME](https://github.com/cnr-isti-vclab/openlime)

定位：
- 后续Web查看器重点方向。
- 适合高分辨率瓦片、交互查看、标注和发布。

需要评估：
- RTI格式支持。
- 瓦片格式：DeepZoom、IIIF等。
- WebGL渲染能力。
- 标注和测量扩展可能性。

## 公开数据集

### CHI Fish Fossil Sample

来源：[RTIBuilder Example Files](https://culturalheritageimaging.org/What_We_Offer/Downloads/Process/)

特点：
- 36张JPEG照片。
- 分辨率有2000和1000版本。
- 适合第一次跑通RTIBuilder/Relight流程。

实验目标：
- 完整跑通RTI处理。
- 检查反光球检测和光照方向估计。
- 对比RTIViewer和Relight/OpenLIME查看效果。

### VAT 15829 RTI Dataset

来源：[VAT 15829 RTI dataset](https://datastore.uni-muenster.de/records/gmcn0-sac84)

特点：
- 楔形文字泥板。
- 与碑刻/刻痕识读较接近。
- 适合研究浅刻文字的RTI增强。

实验目标：
- 观察不同增强模式对文字笔画的影响。
- 记录哪些角度最适合识读。
- 尝试导出增强图和线图。

### VAT 18242 RTI Dataset

来源：[VAT 18242 RTI dataset](https://datastore.uni-muenster.de/records/5n84d-0eg89)

特点：
- 大型数据集。
- 文件体量大，适合后期性能、存储和批处理测试。

实验目标：
- 暂不作为第一轮下载对象。
- 后续用于评估数据管理、处理耗时和Web发布。

## 自建小样本数据

第一批自采对象建议：
- 硬币：纹理清楚，适合检查流程。
- 刻字石片：接近碑刻。
- 手工刻痕板：可控制刻痕深浅。
- 拓片打印件：用于比较二维拓片和RTI增强。
- 风化石材或粗糙砖块：用于测试噪声和误增强。

自采数据命名建议：

```text
dataset_id/
  raw/
    img_0001.jpg
    img_0002.jpg
  metadata/
    capture.json
    lights.csv
  processed/
    relight/
    ptm/
    normals/
    exports/
  notes/
    experiment.md
```

## 基线复现实验

### 实验A：官方样例跑通

目标：
- 下载CHI fish fossil sample。
- 使用Relight或RTIBuilder处理。
- 使用RTIViewer或OpenLIME查看。
- 输出处理记录。

成功标准：
- 得到可交互重打光文件。
- 能查看至少2种增强模式。
- 能记录输入照片数、处理参数、输出文件。

### 实验B：刻痕类公开数据

目标：
- 选择VAT楔形文字数据。
- 重点观察文字刻痕增强。
- 截取几组典型效果图。

成功标准：
- 能说明RTI对刻痕识读的帮助。
- 能比较普通照片、斜光视图、增强视图。

### 实验C：自建小样本

目标：
- 用低成本手持光源采集20-50张图。
- 跑通光照估计和拟合。
- 输出增强图和数字拓片初稿。

成功标准：
- 自采样本能产生有效重打光或法线图。
- 能发现采集问题并更新SOP。

## 工具评估表

| 工具 | 主要用途 | 优势 | 风险 | 是否进入后续开发 |
| --- | --- | --- | --- | --- |
| RelightLab | 处理RTI和法线 | 现代、开源、格式多 | 需验证Windows流程 | 优先 |
| Relight CLI | 批处理 | 自动化潜力高 | 参数学习成本 | 优先 |
| RTIViewer | 查看RTI | 经典增强模式 | 较老 | 对照 |
| RTIBuilder | 传统处理 | 文档完整 | 老旧 | 参考 |
| OpenLIME | Web查看 | 现代Web发布 | 集成成本待评估 | 优先 |

## 本阶段交付物

- 工具安装和可用性记录。
- 至少1个公开数据集完整复现实验。
- PTM/HSH/RBF至少2种输出对比。
- 自采小样本采集问题清单。
- 后续软件可复用工具链建议。

## 待办

- [ ] 确认RelightLab在本机或Ubuntu环境中的安装方式。
- [ ] 下载或记录CHI fish fossil sample。
- [ ] 跑通第一套公开数据。
- [ ] 记录处理参数和输出。
- [ ] 评估OpenLIME作为Web查看器的可行性。
