# 02 文化遗产与碑刻案例

## 学习目标

系统学习RTI在文化遗产中的实际应用，重点关注碑刻、墓碑、印章、楔形文字、石质浅浮雕和大型文物。这些案例会帮助我们判断RTI对汉画像石和碑刻微痕扫描的适用边界。

## 案例一：Telmessos碑刻与V-RTI

资料：[Carved in Stone: Field Trials of Virtual RTI in Classical Telmessos](https://avesis.deu.edu.tr/yayin/fd9cf63a-fa5b-47d4-8d40-938510c856f2/carved-in-stone-field-trials-of-virtual-reflectance-transformation-imaging-v-rti-in-classical-telmessos-fethiye)

关注点：
- RTI用于野外碑刻调查。
- 通过重打光发现新铭文、重刻痕迹和palimpsest。
- V-RTI把3D、VR和RTI结合，用于复杂环境。

对我们的启发：
- 汉画像石和碑刻常处于不可移动或光照不可控环境，V-RTI和现场快速采集值得关注。
- 多源数据融合是后续软件工作流方向，不能只停留在单一RTI文件。

需要记录：
- 采集方式。
- 发现文字或图像细节的证据。
- H-RTI和V-RTI对比。
- 野外环境限制。

## 案例二：Tanais陶器印章

资料：[Using RTI to document ancient amphora stamps from Tanais](https://www.sciencedirect.com/science/article/pii/S2352409X21000511)

关注点：
- RTI用于陶器印章、短铭文和压印痕迹。
- 与传统照片、拓片、绘图进行比较。
- RTI不是总能替代传统方法，但能验证和补充识读。

对我们的启发：
- 汉画像石的线刻、浅浮雕和风化文字可以采用“传统拓片/照片 + RTI + 线图”的对照体系。
- 研究型输出不能只给漂亮图，还要能支撑释读过程。

需要记录：
- RTI在多少案例中提高了识读。
- 哪些情况下RTI只是辅助验证。
- 短铭文和图像纹样的增强差异。

## 案例三：墓碑文字与刻工痕迹

资料：[Reflectance Transformation Imaging: Capturing Gravestone Detail](https://www.debs.ac.uk/files/Mytum_et_al_2017-RTI.pdf)

关注点：
- 风化墓碑文字、苔藓遮挡、石材纹理干扰。
- 刻工细节、修正痕迹、浅刻线。
- Specular enhancement等增强模式在文字识读中的作用。

对我们的启发：
- 汉画像石常见风化、裂隙、石质颗粒和拓片遮蔽问题，墓碑案例很接近。
- 需要把“刻痕细节”和“材质噪声”区分开，避免过增强造成误读。

需要记录：
- 不同石材对RTI效果的影响。
- 苔藓、污渍、裂缝的处理。
- 增强图和人工释读之间的关系。

## 案例四：碑铭学中的RTI方法综述

资料：[RTI as a New Documentation and Analysis Method in Epigraphical Studies](https://dergipark.org.tr/en/download/article-file/3691809)

关注点：
- RTI在碑铭学中的方法论位置。
- 非接触、无损、可重复查看。
- 与显微镜、斜光摄影、多光谱和3D扫描的关系。

对我们的启发：
- 后续软件要支持“研究过程记录”，不仅是生成图像。
- 对碑刻和汉画像石而言，数据可追溯性非常关键。

需要记录：
- RTI的优势、局限和适用条件。
- 与其他文物记录方法的互补关系。
- 论文中提到的采集参数。

## 案例五：大型文物和浅浮雕

资料：[High Quality PTM Acquisition for Large Objects](http://vcg.isti.cnr.it/Publications/2006/DCCS06/)

关注点：
- 中大型文物的RTI/PTM采集问题。
- 光照数量和位置对质量的影响。
- 大尺寸对象的高分辨率浏览。

对我们的启发：
- 汉画像石可能尺寸较大，需要考虑分区采集、拼接和瓦片发布。
- LED半球适合小件，野外大件可能需要移动光源或多区块方案。

需要记录：
- 大对象的光源距离和角度策略。
- 质量评估指标。
- 高分辨率PTM浏览方式。

## 案例比较表

| 案例 | 对象 | 主要问题 | RTI价值 | 对汉画像石启发 |
| --- | --- | --- | --- | --- |
| Telmessos | 石刻碑铭 | 野外环境、重刻、磨损 | 发现新读法 | 适合不可移动石刻 |
| Tanais | 陶器印章 | 短铭文、压印浅 | 验证释读 | 适合浅刻线和图案 |
| Gravestone | 墓碑 | 风化、苔藓、石材噪声 | 增强文字和刻工 | 适合风化碑刻 |
| Epigraphy review | 碑铭学 | 方法论与记录规范 | 建立研究流程 | 支持SOP设计 |
| Large objects | 大型浅浮雕 | 尺寸、光照、浏览 | 高分辨率RTI | 支持分区采集 |

## 本阶段交付物

- 至少5个RTI文化遗产案例摘要。
- 案例中采集方式、处理工具、输出类型的对比表。
- RTI适合/不适合文物类型的初步判断。
- 对汉画像石和碑刻的可迁移经验清单。

## 待办

- [ ] 阅读Telmessos V-RTI案例并摘录采集流程。
- [ ] 阅读Tanais陶器印章案例并整理传统方法对比。
- [ ] 阅读墓碑RTI案例并记录增强模式。
- [ ] 阅读碑铭学RTI综述。
- [ ] 阅读大型对象PTM采集论文。
