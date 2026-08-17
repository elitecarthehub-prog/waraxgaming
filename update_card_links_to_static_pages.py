import glob
import re

files = [
    r"c:\Users\arthe\Downloads\New folder (3)\index.html",
    r"c:\Users\arthe\Downloads\New folder (3)\index (3).html",
    r"c:\Users\arthe\Downloads\New folder (3)\consoles.html",
    r"c:\Users\arthe\Downloads\New folder (3)\controllers.html",
    r"c:\Users\arthe\Downloads\New folder (3)\headsets.html",
    r"c:\Users\arthe\Downloads\New folder (3)\hardware.html",
    r"c:\Users\arthe\Downloads\New folder (3)\games.html",
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace onclick product links to point to products/product-${item.id}.html
    new_content = content.replace("onclick=\"window.location.href='product.html?id=${item.id}'\"", "onclick=\"window.location.href='products/product-${item.id}.html'\"")
    new_content = new_content.replace("href=\"product.html?id=${item.id}\"", "href=\"products/product-${item.id}.html\"")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated product card links across all catalog pages to point to static physical product HTML files!")
