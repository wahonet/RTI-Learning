# Relic2Contour: Salient contour detection in relics using semi-supervised generative adversarial networks based on knowledge sharing

来源：[npj Heritage Science, 2025](https://www.nature.com/articles/s40494-025-01606-0)

PDF状态：Nature PDF直链返回的文件在本机不可读，未保留损坏文件；已阅读网页全文和PDF抽取文本。

## 论文在做什么

Relic2Contour关注“文物图像到清晰轮廓线图”的自动生成。文物表面常有颜料斑驳、裂缝、病害、污渍和纹理噪声，这些干扰会和真实轮廓交织在一起。作者提出半监督GAN框架，希望在标注数据有限时生成更清晰、更稳定的文物轮廓图。

## 方法

核心结构是双分支联合训练：

- 监督分支：使用干净文物图和对应轮廓图进行训练。
- 无监督分支：处理带病害、噪声或风格复杂的文物图像。

生成器中包含两条信息流：

- CGF，contour generation flow，负责轮廓生成。
- AGF，auxiliary gradient flow，负责梯度/边缘辅助特征。

关键模块：

- CAT，coordinate attention transfer，在空间方向上传递AGF中的有效低层特征。
- Bi-GTF，bidirectional gated transposed fusion，双向门控融合梯度特征和文物特征。

## 对汉画像石的价值

汉画像石研究高度依赖线图和拓片。Relic2Contour的意义不只是“把照片变成线稿”，而是提供了一个处理病害、裂缝、纹理噪声的思路。汉画像石常见石材颗粒、风化裂隙、拓印墨迹、低浮雕边界不清等问题，这类半监督框架比普通Canny、Sobel或单纯ControlNet更适合研究。

可迁移流程：

- 原始照片、RTI增强图、法线阴影图作为输入。
- 人工线图或高质量拓片作为少量监督样本。
- 模型输出候选线图。
- 人工校正后进入正式研究线图和IIML标注。

## 局限

- 论文面向广义文物图像，不是专门面向汉画像石。
- 训练仍需要一定数量的高质量成对样本。
- 自动轮廓不能直接等同于考古线图，需要人工确认图像学含义。
- 代码和数据集未在检索结果中发现稳定公开仓库。

## 后续任务

- 建立“汉画像石增强图-人工线图”小样本对。
- 用传统边缘检测、SAM、Relic2Contour类GAN、扩散模型线图生成做对比。
- 输出时保留候选线、人工确认线和废弃线，避免把AI误线混入正式释读。
