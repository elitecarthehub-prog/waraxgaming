import glob
import os
import re
import subprocess

html_files = glob.glob(r"c:\Users\arthe\Downloads\New folder (3)\*.html")

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    # Extract all inline script blocks
    script_blocks = re.findall(r'<script>(.*?)</script>', txt, flags=re.DOTALL)
    
    for idx, script in enumerate(script_blocks):
        if not script.strip():
            continue
        temp_file = r"c:\Users\arthe\Downloads\New folder (3)\temp_test.js"
        with open(temp_file, 'w', encoding='utf-8') as tf:
            tf.write(script)
        
        res = subprocess.run(['node', '--check', temp_file], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[FAIL] SYNTAX ERROR in {os.path.basename(path)} (Script #{idx+1}):")
            print(res.stderr[:300])
        else:
            print(f"[OK] {os.path.basename(path)} (Script #{idx+1})")

if os.path.exists(r"c:\Users\arthe\Downloads\New folder (3)\temp_test.js"):
    os.remove(r"c:\Users\arthe\Downloads\New folder (3)\temp_test.js")
