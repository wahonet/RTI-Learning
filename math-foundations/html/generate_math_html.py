from __future__ import annotations

from html import escape
from pathlib import Path


OUT = Path(__file__).resolve().parent


LESSONS = [
    {
        "file": "01-vectors-light-normals.html",
        "title": "01 向量、光照方向和表面法线",
        "tag": "线性代数入门",
        "summary": "RTI 和光度立体里，光照方向、相机方向、表面法线都可以看成空间里的箭头。先会读这些箭头，后面的公式才不吓人。",
        "sections": [
            ("向量是什么", "向量就是带方向的量。二维向量写成 (x, y)，三维向量写成 (x, y, z)。你可以把它想成从一个点指向另一个方向的箭头。"),
            ("光照方向为什么是向量", "一盏灯从左上方照到石刻，我们关心的是光从哪个方向来。这个方向可以写成 L=(lx, ly, lz)。RTI 的每张照片都对应一个光照方向。"),
            ("表面法线是什么", "法线是垂直于表面的方向。平的石面法线大致朝向相机；刻痕边缘会让法线偏转。法线图就是把每个像素的表面方向保存为颜色或数值。"),
            ("论文里怎么出现", "看到 light direction、surface normal、unit vector、normalize，就把它们翻译成方向箭头。不要先纠结公式，先画箭头。"),
            ("在项目里怎么用", "采集时记录每张图的光照方向；处理时输出法线图；解释时用法线变化判断刻痕、边缘和微小起伏。"),
        ],
        "formula": "I = L n",
        "formula_explain": "最粗略地读：亮度 I 由光照方向 L 和表面法线 n 的关系决定。真实论文会更复杂，但直觉从这里开始。",
    },
    {
        "file": "02-dot-product-raking-light.html",
        "title": "02 点积、夹角和斜光",
        "tag": "向量几何",
        "summary": "点积用来计算两个方向有多接近。斜光为什么能显出刻痕，本质上就是光照方向和表面法线夹角变化被放大了。",
        "sections": [
            ("点积是什么", "两个单位向量 a 和 b 的点积等于它们夹角的余弦。方向越接近，点积越大；方向越垂直，点积越接近 0。"),
            ("它为什么和亮度有关", "漫反射模型里，表面越正对光源越亮，越侧对光源越暗。这个“正对程度”就可以用点积表示。"),
            ("斜光为什么有用", "浅刻边缘会让表面方向突然变化。正面光不容易显出来，低角度斜光会制造明显阴影，所以碑刻和汉画像石常用斜光观察。"),
            ("RTI的优势", "传统斜光照片只有一个角度，RTI 保存很多角度。后期移动虚拟光源，就能反复寻找最能显出细节的方向。"),
            ("风险", "阴影更明显不代表信息更真实。斜光也会放大石材颗粒、污渍、裂纹和算法伪影。"),
        ],
        "formula": "I = ρ (L · n)",
        "formula_explain": "ρ 是表面自身反照率，L·n 是光照方向和表面法线的点积。读成：亮度约等于材质亮度乘以朝光程度。",
    },
    {
        "file": "03-least-squares-fitting.html",
        "title": "03 最小二乘和拟合",
        "tag": "高数+线代",
        "summary": "PTM、HSH、光度立体、相机标定、神经网络都在做一件事：找一组参数，让预测结果和真实照片之间的误差尽量小。",
        "sections": [
            ("什么是拟合", "你拍了很多光照方向下的同一个像素，希望用一个公式预测它在任意光照下的亮度。照片有噪声，所以公式不可能完美，只能尽量接近。"),
            ("误差是什么", "预测值和真实值的差就是误差。每张照片都有一个误差，算法要让整体误差小。"),
            ("为什么叫最小二乘", "把每个误差平方后加起来，再让这个总和最小。平方能避免正负抵消，也会更惩罚大错误。"),
            ("PTM里怎么用", "PTM 对每个像素拟合一个二次多项式，求出一组系数。系数拟合得好，虚拟光照才自然。"),
            ("光度立体里怎么用", "多张照片提供多个亮度方程，法线通常通过最小二乘估计。灯位错误或阴影严重会让拟合结果变差。"),
        ],
        "formula": "minimize  e1² + e2² + ... + en²",
        "formula_explain": "读成：调整参数，让所有观测的误差平方和最小。",
    },
    {
        "file": "04-matrices-photometric-stereo.html",
        "title": "04 矩阵和光度立体",
        "tag": "线性代数",
        "summary": "光度立体把多张照片、多盏灯、多像素组织成矩阵。矩阵不是玄学，它只是把很多个方程整齐放在一起。",
        "sections": [
            ("为什么需要矩阵", "一个像素在 16 盏灯下有 16 个亮度值。一个对象有几百万像素。矩阵可以把这些数据整齐地表示和计算。"),
            ("L矩阵是什么", "L 通常表示光照方向矩阵。每一行可以理解为一盏灯的方向。"),
            ("I向量是什么", "I 是某个像素在不同光照下的亮度列表。"),
            ("n向量是什么", "n 是要估计的表面法线，通常有 x、y、z 三个分量。"),
            ("为什么灯至少要三盏", "法线有三个未知分量。理论上至少需要三个独立光照方向；实际为了抗噪声，通常用更多灯，再用最小二乘。"),
        ],
        "formula": "I = L n",
        "formula_explain": "读成：很多张照片的亮度 I，由很多个光照方向 L 和一个表面法线 n 共同决定。",
    },
    {
        "file": "05-gradient-normal-height.html",
        "title": "05 梯度、法线和高度图",
        "tag": "多元微积分",
        "summary": "高度图可以看成 z=h(x,y)。梯度描述这个表面往 x 和 y 方向怎么倾斜，法线和梯度紧密相关。",
        "sections": [
            ("高度图是什么", "高度图把每个像素对应一个高度值。灰度越亮可以代表越高，越暗代表越低，具体取决于编码。"),
            ("偏导是什么", "偏导描述函数沿某一个方向变化多快。∂h/∂x 是横向坡度，∂h/∂y 是纵向坡度。"),
            ("梯度是什么", "梯度把两个方向的坡度合在一起，告诉你表面往哪里升得最快。"),
            ("法线和梯度", "如果知道表面坡度，就能算表面法线；反过来，如果知道法线，也可以尝试积分恢复高度。"),
            ("为什么积分有风险", "从局部方向恢复整体高度会累积误差。RTI 法线积分出来的高度图不能直接当真值，必须验证。"),
        ],
        "formula": "z = h(x, y),  gradient = (∂h/∂x, ∂h/∂y)",
        "formula_explain": "读成：高度 z 是位置 x,y 的函数；梯度描述这个高度函数在两个方向上的坡度。",
    },
    {
        "file": "06-loss-optimization-ai.html",
        "title": "06 损失函数、优化和AI模型",
        "tag": "优化+机器学习",
        "summary": "YOLO、U-Net、GAN、NeuralRTI、扩散模型都要训练。训练就是定义一个损失函数，再不断调整参数让损失变小。",
        "sections": [
            ("损失函数是什么", "损失函数就是模型错得有多严重的数字。数字越小，说明模型越接近训练目标。"),
            ("优化是什么", "优化就是调整模型参数，让损失函数越来越小。梯度下降是最常见的调整方法。"),
            ("YOLO里的损失", "目标检测通常同时关心分类是否正确、框位置是否准确、目标置信度是否合理。"),
            ("GAN里的损失", "生成器想骗过判别器，判别器想识破生成器。两者互相竞争，得到更像目标风格的线图。"),
            ("文物AI的风险", "损失变小不代表学术真实。AI可能生成合理但不存在的线，所以所有AI输出都应是候选。"),
        ],
        "formula": "parameters ← parameters - learning_rate × gradient",
        "formula_explain": "读成：参数沿着让错误下降最快的方向走一小步，反复很多次。",
    },
    {
        "file": "07-calculus-roadmap.html",
        "title": "07 微积分怎么为RTI服务",
        "tag": "高数路线",
        "summary": "不用把 OpenStax 三本都从头啃完。服务 RTI，最先要懂函数、导数、偏导、梯度、积分和误差变化。",
        "sections": [
            ("函数", "函数描述输入和输出关系。光照方向到像素亮度、位置到高度、参数到误差，都是函数。"),
            ("导数", "导数描述一个量变化时另一个量怎么变。优化、梯度下降和曲面坡度都靠它。"),
            ("积分", "积分可以理解为把很多小变化累积起来。法线积分恢复高度就是一种累积。"),
            ("多元函数", "图像和表面通常有 x,y 两个空间变量。多元函数比一元函数更贴近图像计算。"),
            ("学习顺序", "先 Calculus 1 的函数/导数/积分，再 Calculus 3 的向量/偏导/梯度。Calculus 2 暂时只挑积分技巧和级数直觉。"),
        ],
        "formula": "error = f(parameters)",
        "formula_explain": "读成：误差是参数的函数。训练或拟合就是找参数，让误差变小。",
    },
    {
        "file": "08-reading-formulas.html",
        "title": "08 读论文公式的四步法",
        "tag": "论文阅读方法",
        "summary": "看到公式不要慌。先找输入、未知量、误差、输出。大多数RTI和AI论文公式都能这样拆。",
        "sections": [
            ("第一步：找输入", "输入可能是照片、光照方向、像素坐标、点云、文本提示、已有线图。"),
            ("第二步：找未知量", "未知量可能是 PTM 系数、表面法线、高度、神经网络参数、目标框。"),
            ("第三步：找误差", "论文会定义预测和真实之间的差。看懂误差，就看懂模型在努力优化什么。"),
            ("第四步：找输出", "输出可能是 RTI 文件、法线图、高度图、线图、聚类结果或标注候选。"),
            ("别被符号吓住", "同一个概念不同论文符号可能不同。你要先翻译成中文动作，再回头看符号。"),
        ],
        "formula": "input -> model -> output -> error -> update",
        "formula_explain": "把复杂公式先读成流程图，这是最稳的入门方式。",
    },
]


CSS = """
:root { --bg:#f6f1e9; --paper:#fffdf8; --ink:#26231f; --muted:#6b645d; --line:#d9cdbd; --accent:#9b3f2c; --accent2:#246b61; --soft:#f1e7da; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; line-height:1.75; }
a { color:var(--accent2); text-underline-offset:3px; }
main { max-width:1060px; margin:0 auto; padding:28px 18px 60px; }
.hero { border-bottom:1px solid var(--line); padding-bottom:18px; margin-bottom:18px; }
h1 { font-size:34px; line-height:1.15; margin:0 0 10px; letter-spacing:0; }
h2 { color:var(--accent2); font-size:22px; margin:26px 0 10px; letter-spacing:0; }
h3 { color:#4d5f9f; font-size:17px; margin:0 0 5px; letter-spacing:0; }
p { margin:0 0 12px; }
.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; }
.card,.section,.formula { background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:16px; margin:12px 0; }
.badge { display:inline-block; border:1px solid var(--line); border-radius:5px; padding:2px 8px; color:var(--muted); background:var(--soft); font-size:13px; margin-right:6px; }
.formula { background:#fff6e5; border-color:#e5d4ab; }
code { background:#f3eadc; padding:1px 4px; border-radius:4px; }
nav { display:flex; justify-content:space-between; gap:10px; margin-top:24px; }
nav a { background:var(--paper); border:1px solid var(--line); border-radius:6px; padding:7px 10px; text-decoration:none; color:var(--ink); }
@media (max-width:640px){ main{padding:20px 14px 42px;} nav{flex-direction:column;} }
"""


def lesson_link(lesson: dict) -> str:
    return f'<a href="{lesson["file"]}">{escape(lesson["title"])}</a>'


def render_lesson(lesson: dict, prev_lesson: dict | None, next_lesson: dict | None) -> str:
    sections = "".join(
        f'<section class="section"><h3>{escape(title)}</h3><p>{escape(body)}</p></section>'
        for title, body in lesson["sections"]
    )
    prev_link = f'<a href="{prev_lesson["file"]}">上一课</a>' if prev_lesson else "<span></span>"
    next_link = f'<a href="{next_lesson["file"]}">下一课</a>' if next_lesson else "<span></span>"
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(lesson["title"])}</title>
  <style>{CSS}</style>
</head>
<body>
  <main>
    <header class="hero">
      <p><span class="badge">{escape(lesson["tag"])}</span><span class="badge">中文数学基础</span></p>
      <h1>{escape(lesson["title"])}</h1>
      <p>{escape(lesson["summary"])}</p>
      <p><a href="index.html">返回数学课索引</a> · <a href="../README.md">数学资料说明</a></p>
    </header>
    {sections}
    <section class="formula">
      <h2>公式怎么读</h2>
      <p><code>{escape(lesson["formula"])}</code></p>
      <p>{escape(lesson["formula_explain"])}</p>
    </section>
    <nav>{prev_link}<a href="index.html">索引</a>{next_link}</nav>
  </main>
</body>
</html>
"""


def render_index() -> str:
    cards = "".join(
        f'<article class="card"><h2>{lesson_link(lesson)}</h2><p><span class="badge">{escape(lesson["tag"])}</span></p><p>{escape(lesson["summary"])}</p></article>'
        for lesson in LESSONS
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RTI数学基础中文课</title>
  <style>{CSS}</style>
</head>
<body>
  <main>
    <header class="hero">
      <h1>RTI/光度立体/AI线图数学基础中文课</h1>
      <p>这些页面把英文高数、线代和优化教材中最需要的部分改写成中文小课。你不必先读完整英文 PDF，先按这里的顺序读，遇到论文公式再回查。</p>
      <p><a href="../README.md">数学资料包说明</a> · <a href="../../papers/deep-reading/index.html">论文逐段精读</a></p>
    </header>
    <section class="grid">{cards}</section>
  </main>
</body>
</html>
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for i, lesson in enumerate(LESSONS):
        prev_lesson = LESSONS[i - 1] if i else None
        next_lesson = LESSONS[i + 1] if i + 1 < len(LESSONS) else None
        (OUT / lesson["file"]).write_text(render_lesson(lesson, prev_lesson, next_lesson), encoding="utf-8")
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")


if __name__ == "__main__":
    main()
