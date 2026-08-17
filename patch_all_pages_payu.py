import glob
import os
import re

html_files = [
    r"c:\Users\arthe\Downloads\New folder (3)\index.html",
    r"c:\Users\arthe\Downloads\New folder (3)\index (3).html",
    r"c:\Users\arthe\Downloads\New folder (3)\product.html",
    r"c:\Users\arthe\Downloads\New folder (3)\consoles.html",
    r"c:\Users\arthe\Downloads\New folder (3)\controllers.html",
    r"c:\Users\arthe\Downloads\New folder (3)\headsets.html",
    r"c:\Users\arthe\Downloads\New folder (3)\hardware.html",
    r"c:\Users\arthe\Downloads\New folder (3)\games.html",
]

script_tags = """    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <script src="products.js"></script>
    <script src="payu-checkout.js"></script>"""

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace products.js script tag with crypto-js + products.js + payu-checkout.js
        if 'payu-checkout.js' not in content:
            content = content.replace('<script src="products.js"></script>', script_tags)

        # Replace cart icon onclick with openPayUCheckout()
        content = content.replace('onclick="toggleCartModal()"', 'onclick="openPayUCheckout()"')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Patched PayU script in: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error patching {file_path}: {e}")

print("All HTML pages successfully patched with PayU Payment Gateway integration!")
