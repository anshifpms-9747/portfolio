import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

# Image 1 (Hero - That's what I like)
img1 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pepsi1.png\Screenshot 2026-07-01 133315.png")
width, height = img1.size
img1_cropped = img1.crop((0, 85, width, height))
img1_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pepsi_main_4k.png", quality=100)

# Image 2 (Menu - Our Lineup)
img2 = Image.open(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pepsi1.png\Screenshot 2026-07-01 133356.png")
width, height = img2.size
img2_cropped = img2.crop((0, 85, width, height))
img2_cropped.save(r"C:\Users\LENOVO\.gemini\antigravity\scratch\portfolio\pepsi_sub_4k.png", quality=100)

print("Pepsi images cropped successfully!")
