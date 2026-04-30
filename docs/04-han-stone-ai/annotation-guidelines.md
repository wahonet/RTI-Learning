# 汉画像石YOLO/SAM/IIML标注指南

本指南用于从公开图像或自采RTI增强图中建立第一批汉画像石标注数据。目标是先形成可执行的小闭环，而不是一次完成完整图像学体系。

## 标注原则

- 先粗后细：先bbox，后polygon，再关系。
- 先客观后解释：先标“可见对象”，再标“题材身份”，最后标“文化解释”。
- AI只作候选：YOLO/SAM/自动线图必须人工审核。
- 绑定资源版本：原图、RTI增强图、拓片、线图的坐标不能混用。
- 保留负例：误检、伪线、错误分割也应记录，用于改进模型。

## 第一版类别

建议YOLO第一版只做7类：

```text
0 fuxi_nuwa
1 dancer
2 horse
3 chariot
4 beast
5 building
6 inscription
```

说明：
- `fuxi_nuwa`可以先作为组合类，不拆成伏羲和女娲，降低小样本难度。
- `dancer`用于乐舞百戏中的舞者。
- `horse`和`chariot`可分别训练，也可后续组合成车马出行场景。
- `beast`先覆盖神兽/异兽，第二版再细分虎、龙、鸟等。
- `building`覆盖阙、楼阁、门、建筑构件。
- `inscription`覆盖榜题、题记、铭文区域。

## 什么时候用bbox

适合：
- 目标边界不清但大致区域明确。
- YOLO训练。
- 快速检索。
- 场景级粗定位。

不适合：
- 精细轮廓。
- 刻线。
- 裂隙。
- 多个交叠人物的准确分割。

## 什么时候用polygon

适合：
- 单个人物或器物轮廓。
- 纹样块。
- 病害区域。
- SAM候选mask人工修正。

要求：
- 多边形要闭合。
- 不要为了贴合石材噪声而过多顶点。
- 每个polygon必须绑定图像版本。

## 什么时候用line

适合：
- 刻线。
- 轮廓线。
- 裂隙。
- 工具痕。
- 人工研究线图。

要求：
- 区分`carved_line`和`crack`。
- 区分算法候选线和人工确认线。
- 记录来源：RTI增强图、法线图、拓片或原图。

## 标注流程

### 1. 准备图像

每张图像记录：
- 来源URL或采集批次。
- 版权状态。
- 图像版本：原图、拓片、RTI增强图、线图。
- 分辨率。
- 是否可公开。

### 2. 粗标bbox

工具：
- AnyLabeling。
- CVAT。
- Label Studio。

输出：
- YOLO格式。
- 或COCO格式。

### 3. SAM细化

方式：
- 用bbox提示SAM生成mask。
- 或用点提示局部对象。
- 对mask做人工修正。

注意：
- SAM容易把裂缝和石材纹理吞进目标。
- 对浅刻边界不要过度相信自动mask。

### 4. IIML转换

将标注转为：

```json
{
  "resourceId": "resource-enhanced-001",
  "target": {
    "type": "BBox",
    "xywh": [0, 0, 100, 100]
  },
  "semantics": {
    "label": "fuxi_nuwa",
    "interpretationLevel": "iconographical"
  },
  "generation": {
    "method": "manual",
    "reviewStatus": "reviewed"
  }
}
```

### 5. 审核

每条标注状态：
- `candidate`：候选。
- `reviewed`：已审核。
- `rejected`：已拒绝。
- `disputed`：有争议。

## 数据集划分

第一版小样本：

```text
images/
  train/
  val/
  test/
labels/
  train/
  val/
  test/
data.yaml
```

建议：
- 训练集70%。
- 验证集20%。
- 测试集10%。
- 同一件文物的相似图不要同时进入训练和测试，避免虚高。

## `data.yaml`模板

```yaml
path: ./han-stone-yolo-v0
train: images/train
val: images/val
test: images/test
names:
  0: fuxi_nuwa
  1: dancer
  2: horse
  3: chariot
  4: beast
  5: building
  6: inscription
```

## 质量检查

每批标注检查：
- 类别是否一致。
- bbox是否覆盖完整目标。
- polygon是否闭合。
- 是否误把裂缝当轮廓。
- 是否误把拓片墨迹当刻线。
- 是否记录图像来源。
- 是否有重复图像泄漏到不同集合。

## 第一批任务

- [ ] 从Wikimedia和可公开资源选20-50张图。
- [ ] 按7类做bbox。
- [ ] 选10张做SAM polygon。
- [ ] 导出YOLO格式。
- [ ] 转换至少5条IIML JSON-LD。
- [ ] 写一份错误案例记录。

## 后续扩展

第二版类别：
- `musician`
- `rider`
- `bird`
- `dragon`
- `tiger`
- `attendant`
- `border_pattern`
- `cloud_pattern`

第三版加入关系：
- `faces`
- `holds`
- `rides`
- `pulls`
- `above`
- `below`
- `partOf`
- `contains`
