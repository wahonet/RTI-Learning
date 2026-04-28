$ErrorActionPreference = "Stop"

python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e
python tools\stele_enhance.py inputs\image2_b842e.png -o outputs\sample_b842e_crop --roi 850 100 3000 1900

Write-Host "Done. Open outputs\sample_b842e\contact_sheet.jpg and outputs\sample_b842e_crop\contact_sheet.jpg"
