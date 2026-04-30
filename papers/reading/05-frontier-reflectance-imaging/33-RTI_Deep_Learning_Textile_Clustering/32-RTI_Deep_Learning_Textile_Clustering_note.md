# Beyond relighting: RTI for clustering fragmented heritage textiles using deep learning

来源：[npj Heritage Science, 2026](https://www.nature.com/articles/s40494-026-02326-9)

代码仓库：[akhawaja2014/Beyond-Relighting](https://github.com/akhawaja2014/Beyond-Relighting)

PDF状态：网页可读；PDF下载速度过慢且中断，未保留不完整文件。

## 论文在做什么

论文把RTI从“交互重打光”推进到“计算分析”。作者使用RTI数据和深度学习对破碎历史纺织品进行聚类，帮助判断碎片之间的关系和重组可能性。

## 方法

流程大致为：

- 对纺织品碎片采集RTI数据。
- 使用HSH对RTI数据建模。
- 从建模后的RTI数据中提取深度特征。
- 用降维方法可视化特征空间。
- 评估碎片聚类效果，并与RGB照片做比较。

论文结论认为RTI包含比普通RGB更丰富的表面几何和反射信息，因此在碎片聚类上优于单张照片。

## 对汉画像石的价值

这篇论文的意义很大：RTI不只是让人看得清，也可以成为AI输入数据。对汉画像石而言，可考虑：

- 用RTI/HSH系数作为图像检索特征。
- 对相似纹样、边框、车马、人物姿态做聚类。
- 比较普通照片、拓片、RTI增强图、法线图的检索效果。
- 用RTI特征辅助残石拼合或同题材分类。

## 与本项目的关系

本项目后续可以建立“Beyond relighting”路线：

```text
多光照采集
  -> RTI/HSH/RBF/法线图
  -> 特征提取
  -> 聚类/检索/相似图像发现
  -> IIML语义标注和人工确认
```

## 局限

- 研究对象是纺织品，不是石刻。
- 聚类结果需要专业解释，不能自动等同于同源或同题材。
- 代码仓库因网络问题尚未下载到本地，应后续补充。

## 后续任务

- 下载并复现`Beyond-Relighting`仓库。
- 用公开RTI数据测试HSH特征聚类。
- 设计汉画像石纹样检索小实验。
