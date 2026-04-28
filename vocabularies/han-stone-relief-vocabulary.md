# 汉画像石标注词表草案

本词表用于YOLO/SAM/IIML标注、图像学整理和后续知识图谱。它不是正式学术分类，第一版目标是让图像标注可执行、可迭代、可和外部词表映射。

## 设计原则

- 先少后多：第一版只保留高频、可识别、可训练的类别。
- 分层表达：不要把几何元素、图像题材、图像学解释混在同一级标签中。
- 保留证据：每个解释都应能回到原图、RTI增强图、拓片、线图或文献。
- 允许分歧：不同研究者的不同释读应并存，不覆盖。
- AI候选：YOLO/SAM结果默认是候选，需要人工确认。

## 标注层级

### 1. Whole 整体层

用于描述整件对象或整幅画面。

建议字段：
- `object_type`：画像石、画像砖、墓门、祠堂构件、碑刻、拓片。
- `material`：石、砖、拓纸、数字图像。
- `technique`：浅浮雕、线刻、减地平雕、阴线刻、阳线刻、拓印。
- `period`：西汉、东汉、汉代、后世摹拓。

### 2. Scene 场景层

用于描述局部叙事或题材单元。

第一批场景类：
- `fuxi_nuwa_scene`：伏羲女娲图。
- `music_dance_scene`：乐舞百戏。
- `chariot_horse_scene`：车马出行。
- `hunting_scene`：狩猎。
- `banquet_scene`：宴饮。
- `procession_scene`：仪仗/出行。
- `mythic_immortal_scene`：神仙/升仙。
- `architectural_scene`：楼阁、阙、门、院落。
- `ritual_scene`：祭祀/礼仪。
- `inscription_zone`：铭文/榜题区域。

### 3. Figure 单体层

用于YOLO bbox、SAM polygon和人工多边形。

第一批目标检测类：
- `fuxi`：伏羲。
- `nuwa`：女娲。
- `dancer`：舞者。
- `musician`：乐人。
- `rider`：骑者。
- `horse`：马。
- `chariot`：车。
- `bird`：鸟。
- `dragon`：龙。
- `tiger`：虎。
- `beast`：神兽/异兽。
- `attendant`：侍从。
- `building`：建筑构件。
- `inscription`：文字/榜题。

### 4. Component 组成层

用于细粒度研究和形相学。

人物：
- `head`：头部。
- `face`：面部。
- `arm`：手臂。
- `hand`：手。
- `body`：身体。
- `tail`：蛇尾/兽尾。
- `clothing`：衣纹。
- `headdress`：冠帽。

器物：
- `instrument`：乐器。
- `drum`：鼓。
- `weapon`：兵器。
- `vessel`：器皿。
- `wheel`：车轮。
- `canopy`：车盖。

纹样：
- `border_pattern`：边框纹。
- `cloud_pattern`：云气纹。
- `arc_pattern`：连弧纹。
- `geometric_pattern`：几何纹。
- `sun_moon_symbol`：日月符号。

### 5. Trace 微痕层

用于RTI、法线图、数字拓片和微痕研究。

建议类别：
- `carved_line`：刻线。
- `relief_edge`：浮雕边界。
- `tool_mark`：工具痕。
- `crack`：裂隙。
- `weathering`：风化。
- `abrasion`：磨损。
- `ink_residue`：拓印墨迹。
- `surface_noise`：石材颗粒/噪声。
- `repair_trace`：修复痕迹。

## 解释层级

### 前图像层 pre-iconographical

只描述可见对象：
- 人物。
- 马。
- 车。
- 树。
- 建筑。
- 线条。
- 裂缝。

### 图像志层 iconographical

描述题材和身份：
- 伏羲女娲。
- 乐舞百戏。
- 车马出行。
- 升仙。
- 神兽。
- 门阙。

### 图像学层 iconological

描述文化解释：
- 宇宙观。
- 墓葬礼仪。
- 祥瑞。
- 身份表达。
- 地域风格。
- 孝道/伦理叙事。

## YOLO第一版类别建议

第一版只建议训练以下类别：

```text
0 fuxi_nuwa
1 dancer
2 horse
3 chariot
4 beast
5 building
6 inscription
```

原因：
- 目标相对明确。
- 具有图像学价值。
- 可从公开资料中找到样本。
- 适合bbox粗定位。

第二版再扩展：

```text
7 musician
8 rider
9 bird
10 dragon
11 tiger
12 attendant
13 border_pattern
14 cloud_pattern
```

## IIML字段映射建议

```json
{
  "label": "fuxi_nuwa",
  "prefLabel": "伏羲女娲",
  "altLabel": ["伏羲女娲图", "伏羲女娲像"],
  "structuralLevel": "scene",
  "interpretationLevel": "iconographical",
  "broader": "mythic_immortal_scene",
  "closeMatch": [],
  "source": "local-vocabulary-v0.1",
  "reviewStatus": "draft"
}
```

## 外部词表映射

优先参考：
- Chinese Iconography Thesaurus (CIT)。
- Wikidata。
- Getty AAT。
- ICON Ontology。
- Iconclass中可对应的通用概念。

映射原则：
- 有精确对应时使用`exactMatch`。
- 只有近似对应时使用`closeMatch`。
- 中国本土图像学概念不要强行映射到西方分类。

## 标注审核规则

### 候选 candidate

来自YOLO、SAM、边缘检测、自动线图或未经审核的人工草标。

### 已审核 reviewed

人工确认几何和标签基本正确，但不一定代表最终学术解释。

### 已拒绝 rejected

误检、误分割、伪线条、错误释读。

### 有争议 disputed

几何对象存在，但图像学解释存在分歧。

## 后续任务

- [ ] 把词表转为CSV或JSON-LD。
- [ ] 从河南汉画像石数据库和CIT抽取常用题材词。
- [ ] 为第一版YOLO类别收集样例图。
- [ ] 建立标注指南：何时框整体，何时框局部。
- [ ] 建立“裂缝/刻线/石材纹理”的判别规则。
