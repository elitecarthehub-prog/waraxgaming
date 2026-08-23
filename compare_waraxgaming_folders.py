import os
import filecmp

DIR_A = r"c:\Users\arthe\Downloads\New folder (3)"
DIR_B = r"c:\Users\arthe\Downloads\waraxgaming"

files_a = set(os.listdir(DIR_A))
files_b = set(os.listdir(DIR_B))

print("Files in waraxgaming but not in New folder (3):", files_b - files_a)
print("Files in New folder (3) but not in waraxgaming:", files_a - files_b)

common_files = [f for f in files_a.intersection(files_b) if os.path.isfile(os.path.join(DIR_A, f))]
differing = []
for f in common_files:
    path_a = os.path.join(DIR_A, f)
    path_b = os.path.join(DIR_B, f)
    if not filecmp.cmp(path_a, path_b, shallow=False):
        differing.append(f)

print(f"\nFound {len(differing)} files with differences:")
for f in differing:
    size_a = os.path.getsize(os.path.join(DIR_A, f))
    size_b = os.path.getsize(os.path.join(DIR_B, f))
    print(f"  - {f} (New folder 3: {size_a} bytes | waraxgaming: {size_b} bytes)")
