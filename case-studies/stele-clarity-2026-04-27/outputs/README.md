# Local Outputs

图像增强输出默认不纳入 Git 跟踪。它们目前保留在本地旧目录：

```text
E:\relics-align2\stele_clarity_research_2026-04-27\outputs
```

这些输出可以通过脚本重新生成：

```powershell
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e_crop --roi 850 100 3000 1900
```
