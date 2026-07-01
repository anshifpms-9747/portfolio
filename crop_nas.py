import sys
import subprocess
import os

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

# Image 1 (Hero)
img1 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\New folder\Screenshot 2026-07-01 134157.png")
width, height = img1.size
img1_cropped = img1.crop((0, 85, width, height))
img1_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\nas_main_4k.png", quality=100)

# Image 2 (Sub)
img2 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\New folder\Screenshot 2026-07-01 134217.png")
width, height = img2.size
img2_cropped = img2.crop((0, 85, width, height))
img2_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\nas_sub_4k.png", quality=100)

print("NAS images cropped successfully!")
