import glob
import os

files = [
    r"c:\Users\arthe\Downloads\New folder (3)\index.html",
    r"c:\Users\arthe\Downloads\New folder (3)\index (3).html",
    r"c:\Users\arthe\Downloads\New folder (3)\consoles.html",
    r"c:\Users\arthe\Downloads\New folder (3)\controllers.html",
    r"c:\Users\arthe\Downloads\New folder (3)\headsets.html",
    r"c:\Users\arthe\Downloads\New folder (3)\hardware.html",
    r"c:\Users\arthe\Downloads\New folder (3)\games.html",
    r"c:\Users\arthe\Downloads\New folder (3)\product.html",
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Link cards to product-${item.id}.html
    new_content = content.replace("products/product-${item.id}.html", "product-${item.id}.html")
    new_content = new_content.replace("product.html?id=${item.id}", "product-${item.id}.html")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated product links in: {os.path.basename(file_path)}")

print("All catalog cards connected to product-1.html ... product-226.html!")
