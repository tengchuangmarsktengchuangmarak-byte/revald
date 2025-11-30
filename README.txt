Your website is ready! Open `index.html` in a browser to see it.

Scripts:
- `scripts/convert_images.py` - converts PNG images to JPG (already present)
- `scripts/recolor_images.py` - recolors red-like areas in `logo.jpg` and `giftcard.jpg` to Aldi-themed blue and saves as `logo_blue.jpg` and `giftcard_blue.jpg`.

Run these commands in PowerShell (from repo root):
```powershell
python -m pip install -r requirements.txt
python .\scripts\recolor_images.py
```

These scripts will create `logo_blue.jpg` and `giftcard_blue.jpg` and the `index.html` file references those new files.