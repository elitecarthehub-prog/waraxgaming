import re

files = [
    r"c:\Users\arthe\Downloads\New folder (3)\controllers.html",
    r"c:\Users\arthe\Downloads\New folder (3)\games.html",
    r"c:\Users\arthe\Downloads\New folder (3)\hardware.html",
    r"c:\Users\arthe\Downloads\New folder (3)\headsets.html",
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    # Find the end of script tag and replace everything after render function closing brace with clean </script>
    # Match from "to cart!" or orphan string up to </script>
    cleaned = re.sub(r'\s*" to cart!.*?</script>', '\n    </script>', txt, flags=re.DOTALL)
    cleaned = re.sub(r'\s*</span><span class="font-bold text-primary".*?</script>', '\n    </script>', cleaned, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

print("Fixed script ends for all 4 files!")
