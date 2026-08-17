import glob
import re

files = [
    r"c:\Users\arthe\Downloads\New folder (3)\index.html",
    r"c:\Users\arthe\Downloads\New folder (3)\index (3).html",
    r"c:\Users\arthe\Downloads\New folder (3)\product.html",
    r"c:\Users\arthe\Downloads\New folder (3)\consoles.html",
    r"c:\Users\arthe\Downloads\New folder (3)\controllers.html",
    r"c:\Users\arthe\Downloads\New folder (3)\headsets.html",
    r"c:\Users\arthe\Downloads\New folder (3)\hardware.html",
    r"c:\Users\arthe\Downloads\New folder (3)\games.html",
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean orphaned lines between last function and </script>
    content = re.sub(r'// Cart Logic.*?</script>', '</script>', content, flags=re.DOTALL)
    content = re.sub(r'</script>\s*</script>', '</script>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML script tags cleaned!")
