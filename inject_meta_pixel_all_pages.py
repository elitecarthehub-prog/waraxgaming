import os
import re

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"
PIXEL_ID = "1596400438741187"

PIXEL_BASE_CODE = f"""<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

def inject_pixel_into_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing meta pixel code block if present
    content = re.sub(r'<!-- Meta Pixel Code -->.*?<!-- End Meta Pixel Code -->', '', content, flags=re.DOTALL)
    content = re.sub(r'fbq\([^\)]+\);', '', content)

    # Insert right before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{PIXEL_BASE_CODE}\n</head>')
    else:
        content = PIXEL_BASE_CODE + '\n' + content

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Process all Root HTML files
root_htmls = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.html')]
for file_path in root_htmls:
    inject_pixel_into_html(file_path)
    print(f"Injected Meta Pixel ({PIXEL_ID}) into: {os.path.basename(file_path)}")

# 2. Process all products/*.html files
products_dir = os.path.join(ROOT, "products")
if os.path.exists(products_dir):
    p_files = [os.path.join(products_dir, f) for f in os.listdir(products_dir) if f.endswith('.html')]
    for file_path in p_files:
        inject_pixel_into_html(file_path)
    print(f"Injected Meta Pixel ({PIXEL_ID}) into {len(p_files)} product pages in products/")

print("OK: Meta Pixel base code injected into all website HTML files!")
