import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

# Image 1 (Hero)
img1 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pm_main.png\Screenshot 2026-07-01 125113.png")
width, height = img1.size
# Crop top 85 pixels (approximate height of browser tabs and address bar)
img1_cropped = img1.crop((0, 85, width, height))
# Save with high quality
img1_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pm_hero_4k.png", quality=100)

# Image 2 (Menu)
img2 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pm_main.png\Screenshot 2026-07-01 125138.png")
width, height = img2.size
img2_cropped = img2.crop((0, 85, width, height))
img2_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pm_menu_4k.png", quality=100)

print("Images cropped successfully!")
