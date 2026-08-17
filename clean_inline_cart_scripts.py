import glob
import re
import os

html_files = glob.glob(r"c:\Users\arthe\Downloads\New folder (3)\*.html")

for file_path in html_files:
    if "order-success.html" in file_path:
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove inline addToCart / updateCart / openPayUCheckout / toggleCartModal definitions in script tags
    content = re.sub(r'function addToCart\(id\)\s*\{[^}]*alert\([^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'function updateCart\(\)\s*\{[^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'function toggleCartModal\(\)\s*\{[^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'function openPayUCheckout\(\)\s*\{[^}]*cart-drawer[^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'let cartList = \[\];', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned inline cart overrides in: {os.path.basename(file_path)}")

print("Inline cart overrides cleaned successfully!")
