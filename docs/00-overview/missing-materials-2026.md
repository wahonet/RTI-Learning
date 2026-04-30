# 缺失资料补齐清单 2026

本清单用于继续补齐RTI/PTM、汉画像石、考古线图、AI标注和硬件资料。原则：如果PDF下载失败，不保留损坏文件；先记录稳定页面、DOI、摘要和后续获取方式。

## A级：必须补齐

### 1. Malzbender 2001 `Polynomial Texture Maps`

- 类型：经典论文。
- 重要性：PTM源头论文，理解每像素二次多项式、光照方向参数和反射增强。
- 链接：`https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Malzbender01.pdf`
- 当前状态：网页抽取文本已读，PDF未入库。
- 补齐动作：下载PDF为`papers/23_Malzbender_2001_Polynomial_Texture_Maps.pdf`，生成中文笔记。

### 2. PTM 1.2 File Format

- 类型：格式规范。
- 重要性：理解`.ptm`文件头、格式、scale/bias、系数编码和归档风险。
- 链接：`https://shiftleft.com/mirrors/www.hpl.hp.com/techreports/2001/HPL-2001-104.pdf`
- 当前状态：网页抽取文本已读，PDF未入库。
- 补齐动作：下载PDF并做格式说明，和Relight/OpenLIME格式对照。

### 3. Earl 2010 Archaeological Applications of PTM

- 类型：经典考古应用论文。
- 重要性：把PTM/RTI应用到楔形文字、钱币、岩画、石材、考古记录和传播。
- 链接：`https://eprints.soton.ac.uk/156253/`
- 备选PDF：`https://files01.core.ac.uk/download/pdf/24213.pdf`
- 当前状态：网页抽取文本已读，PDF未入库。
- 补齐动作：下载PDF，生成中文笔记，加入文化遗产案例文档。

### 4. Relight / RelightLab 2026

- 类型：核心工具仓库。
- 重要性：现代RTI主工具，支持RelightLab GUI、CLI、PTM/HSH/RBF、法线图、Web格式。
- 链接：`https://github.com/cnr-isti-vclab/relight`
- 当前状态：代理克隆大仓库卡住，未下载。
- 补齐动作：优先下载Release包；其次下载源码zip；最后再尝试浅克隆。

### 5. OpenLIME 2025

- 类型：Web查看器和论文。
- 重要性：RTI、多光谱、BRDF、神经重光照和标注发布的核心Web框架。
- 仓库：`https://github.com/cnr-isti-vclab/openlime`
- 论文PDF：`https://www.crs4.it/vic/data/papers/dh2025-openlime.pdf`
- 当前状态：网页抽取文本已读，仓库未下载。
- 补齐动作：下载PDF，下载源码，做最小RTI页面示例。

### 6. Han YOLO 2024

- 类型：汉画像石目标检测论文。
- 重要性：目前最直接的汉画像石 + YOLO论文。
- 链接：`https://www.nature.com/articles/s40494-024-01232-2`
- 当前状态：已做笔记，PDF下载中断。
- 补齐动作：补PDF；记录数据集不可公开的问题；按其类别设计本地数据集。

## B级：重要但可后续补

### 7. Relic2Contour 2025

- 类型：AI线图论文。
- 链接：`https://www.nature.com/articles/s40494-025-01606-0`
- 当前状态：已做笔记，PDF下载失败。
- 补齐动作：补PDF；继续查找代码/数据集。

### 8. Archaeological Line Drawings from Sculpture Point Cloud 2025

- 类型：点云到考古线图论文。
- 链接：`https://www.nature.com/articles/s40494-025-01678-y`
- 当前状态：已做笔记，PDF下载失败。
- 补齐动作：补PDF；整理算法伪代码；用于光度立体高度图线提取实验。

### 9. Generating Archaeological Line Drawings from Limited Reference Images 2026

- 类型：扩散模型/LoRA线图论文。
- 链接：`https://www.nature.com/articles/s40494-026-02526-3`
- 当前状态：已做笔记，PDF未稳定下载。
- 补齐动作：补PDF；跟踪代码；评估是否能用汉画像石少样本微调。

### 10. Beyond Relighting 2026

- 类型：RTI + 深度学习聚类论文和仓库。
- 论文：`https://www.nature.com/articles/s40494-026-02326-9`
- 仓库：`https://github.com/akhawaja2014/Beyond-Relighting`
- 当前状态：已做笔记，PDF/仓库未下载。
- 补齐动作：补PDF和代码；用公开RTI数据复现HSH特征聚类。

### 11. Photometric Stereo for Paintings and Drawings 2025

- 类型：光度立体标定论文。
- 链接：`https://www.mdpi.com/2571-9408/8/4/129`
- 当前状态：已做笔记，PDF下载不完整。
- 补齐动作：补PDF；提取灯位/相机/平面标定方法。

### 12. Quantitative RTI Profilometry 2024

- 类型：RTI定量验证论文。
- 链接：`https://epjplus.epj.org/articles/epjplus/abs/2024/09/13360_2024_Article_5522/13360_2024_Article_5522.html`
- 当前状态：只有摘要笔记。
- 补齐动作：获取正式PDF；整理误差指标。

## C级：仓库和工程工具

### 13. AnyLabeling

- 链接：`https://github.com/vietanhdev/anylabeling`
- 用途：本地YOLO/SAM/SAM2/SAM3辅助标注。
- 补齐动作：下载Release或源码；试标20张汉画像石图。

### 14. CVAT

- 链接：`https://github.com/cvat-ai/cvat`
- 用途：正式数据集标注、YOLO/COCO/分割导出、SAM自动标注。
- 补齐动作：Docker启动；建立汉画像石测试任务。

### 15. Label Studio

- 链接：`https://github.com/HumanSignal/label-studio`
- 用途：多类型标注和模型预标注。
- 补齐动作：评估是否比CVAT更适合IIML数据管理。

### 16. ImageJ Photometric Stereo Tools

- 链接：`https://github.com/NU-ACCESS/ImageJ-Photometric-Stereo-tools`
- 用途：文物表面法线/高度实验。
- 补齐动作：下载并用硬币/刻痕板测试。

### 17. RTI硬件仓库

- `https://github.com/BeebBenjamin/RTIPy`
- `https://github.com/leszekmp/artid`
- `https://github.com/nichlock/rti`
- 用途：Arduino、3D打印dome、LED控制、相机触发。
- 补齐动作：提取BOM、灯位数量、控制方式、适合汉画像石的改造点。

## D级：数据集与图像资源

### 18. CHI Fish Fossil Sample

- 用途：第一套RTI处理样例。
- 补齐动作：下载1000px版，不建议把大zip提交到Git。

### 19. VAT 15829 / VAT 18242

- 用途：楔形文字RTI，浅刻文字增强对照。
- 补齐动作：先下载VAT 15829，VAT 18242用于后期性能测试。

### 20. DiLiGenT-Pi

- 用途：近似平面光度立体基准。
- 补齐动作：下载小样本，和自采刻痕板结果比较。

### 21. 河南汉画像石图像数据库

- 链接：`http://www.henanhanhua.com/`
- 用途：汉画像石原石照片、拓片、题材、出土地点、尺寸、技法和著录。
- 补齐动作：整理字段；确认版权和引用规则；不要批量抓取入库。

### 22. 漢代石刻畫象拓本數位典藏

- 链接：`http://rub.ihp.sinica.edu.tw/~hanrelief/h/`
- 用途：史语所汉代石刻画像拓本。
- 补齐动作：整理可用图像、元数据和版权。

### 23. Chinese Iconography Thesaurus (CIT)

- 链接：`https://chineseiconography.org/`
- GitHub：`https://github.com/iconclass/cit`
- 用途：中国图像志词表，映射IIML本地词汇。
- 补齐动作：抽取与汉画像石有关的人物、神话、动物、器物、纹样词。

## 下一轮建议顺序

1. 下载并阅读Malzbender 2001、PTM格式规范、Earl 2010。
2. 下载RelightLab和OpenLIME，做最小工具链演示。
3. 安装AnyLabeling，做20张汉画像石YOLO/SAM小样本。
4. 下载CHI Fish Fossil和DiLiGenT-Pi小样本，做RTI/光度立体实验。
5. 整理河南汉画像石数据库字段，建立本地标注词表。
