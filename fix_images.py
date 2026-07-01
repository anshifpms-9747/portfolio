import os
import re
import shutil
import subprocess

html_file = 'index.html'
assets_dir = 'assets'

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'src="(\.\./\.\./brain/[^"]+)"', content)

for match in matches:
    original_path = match.group(1)
    abs_path = os.path.abspath(os.path.join(os.getcwd(), original_path))
    
    filename = os.path.basename(abs_path)
    new_local_path = os.path.join(assets_dir, filename)
    
    print(f"Copying {abs_path} to {new_local_path}")
    if os.path.exists(abs_path):
        shutil.copy2(abs_path, new_local_path)
    else:
        print(f"WARNING: File not found {abs_path}")
    
    new_src = f'assets/{filename}'
    content = content.replace(original_path, new_src)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Committing and pushing changes...")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Move AI images into project repository for Netlify'])
subprocess.run(['git', 'push', 'origin', 'main'])

print("Fixed images and pushed to GitHub!")
