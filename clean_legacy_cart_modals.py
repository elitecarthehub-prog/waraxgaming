import glob
import os
import re

html_files = glob.glob(r"c:\Users\arthe\Downloads\New folder (3)\*.html")

for file_path in html_files:
    if "order-success.html" in file_path:
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace legacy cart modal blocks if present
    # Legacy cart-drawer pattern
    pattern = r'<!-- Cart Modal -->\s*<div id="cart-drawer".*?</div>\s*</div>'
    new_content = re.sub(pattern, '<!-- PayU Cart & Checkout handled dynamically by payu-checkout.js -->', content, flags=re.DOTALL)

    # Ensure buy now / add to cart buttons call openPayUCheckout() / addToCart()
    new_content = new_content.replace('toggleCartModal()', 'openPayUCheckout()')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned legacy cart modal in: {os.path.basename(file_path)}")

print("Cleaned up legacy cart modals across all pages!")
