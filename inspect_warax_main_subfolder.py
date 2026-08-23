import os
import filecmp

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"
SUB = os.path.join(ROOT, "waraxgaming-main")

sub_files = [f for f in os.listdir(SUB) if os.path.isfile(os.path.join(SUB, f))]
print("Files directly inside waraxgaming-main:")
for f in sub_files:
    root_file = os.path.join(ROOT, f)
    sub_file = os.path.join(SUB, f)
    if os.path.exists(root_file):
        diff = not filecmp.cmp(root_file, sub_file, shallow=False)
        print(f"  - {f}: {'DIFFERENT' if diff else 'Identical'}")
    else:
        print(f"  - {f}: Only in waraxgaming-main")
