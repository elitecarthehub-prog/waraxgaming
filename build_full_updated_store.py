import json
import os
import re

ROOT_DIR = r"c:\Users\arthe\Downloads\New folder (3)"
PRODUCTS_JS = os.path.join(ROOT_DIR, "products.js")
SCRATCH_JSON = os.path.join(ROOT_DIR, "scratch_new_products.json")
IMAGES_DIR   = os.path.join(ROOT_DIR, "images")

def build_all():
    if not os.path.exists(SCRATCH_JSON):
        print("scratch_new_products.json not found!")
        return

    with open(SCRATCH_JSON, 'r', encoding='utf-8') as f:
        products = json.load(f)

    # Map images
    image_files = os.listdir(IMAGES_DIR)
    pid_to_img = {}
    for fname in image_files:
        if fname.endswith(('.jpg', '.png', '.jpeg', '.webp')):
            parts = fname.split('_', 1)
            if len(parts) == 2 and parts[0].isdigit():
                pid_to_img[int(parts[0])] = f"images/{fname}"

    for p in products:
        pid = p['id']
        if pid in pid_to_img:
            p['image'] = pid_to_img[pid]
        elif not p.get('image') or not p['image'].startswith('images/'):
            cat = p.get('sheetCategory', '')
            if cat == 'Games':
                p['image'] = "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800&auto=format&fit=crop"
            elif cat == 'Consoles':
                p['image'] = "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?q=80&w=800&auto=format&fit=crop"
            elif cat == 'Controllers':
                p['image'] = "https://images.unsplash.com/photo-1592840496694-26d035b52b48?q=80&w=800&auto=format&fit=crop"
            elif cat == 'VR':
                p['image'] = "https://images.unsplash.com/photo-1622979135225-d2ba269bc1bd?q=80&w=800&auto=format&fit=crop"
            else:
                p['image'] = "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=800&auto=format&fit=crop"

    # Save products.js
    js_content = "const PRODUCTS_DATA = " + json.dumps(products, indent=2) + ";\n"
    with open(PRODUCTS_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"OK: Saved products.js with {len(products)} items!")

    # Generate 473 HTML files
    count = 0
    for p in products:
        pid = p['id']
        name = p['name']
        brand = p.get('brand', 'WARAX')
        category = p.get('sheetCategory', 'Gaming')
        price = p['price']
        original_price = p.get('originalPrice', price)
        discount = p.get('discount', 0)
        savings = original_price - price
        img_src = p.get('image', 'images/default_game.jpg')
        file_path = os.path.join(ROOT_DIR, f"product-{pid}.html")

        specs_html = f"""
        <div class="border border-white/10 rounded-2xl overflow-hidden mt-6">
            <div class="bg-surface px-5 py-3 border-b border-white/10">
                <h3 class="font-heading font-bold text-white text-sm uppercase tracking-wider">Product Specifications</h3>
            </div>
            <div class="divide-y divide-white/5">
                <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5"><span class="text-slate-400 font-semibold w-1/3">Brand</span><span class="text-white w-2/3 text-right">{brand}</span></div>
                <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5"><span class="text-slate-400 font-semibold w-1/3">Category</span><span class="text-white w-2/3 text-right">{category}</span></div>
                <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5"><span class="text-slate-400 font-semibold w-1/3">Compatibility</span><span class="text-white w-2/3 text-right">{p.get('compatibility', brand)}</span></div>
                <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5"><span class="text-slate-400 font-semibold w-1/3">Original MRP</span><span class="text-white w-2/3 text-right">₹{original_price:,}</span></div>
                <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5"><span class="text-slate-400 font-semibold w-1/3">WARAX Price</span><span class="text-white w-2/3 text-right">₹{price:,} ({discount}% OFF)</span></div>
            </div>
        </div>
        """

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>{name} | WARAX GAMING</title>
    <meta name="description" content="Buy {name} by {brand} at guaranteed best price ₹{price:,} with {discount}% discount on WARAX GAMING India.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ heading: ['Montserrat', 'sans-serif'], body: ['Inter', 'sans-serif'] }},
                    colors: {{ primary: '#991b1b', primaryHover: '#7f1d1d', dark: '#09090b', surface: '#18181b', surfaceHover: '#27272a' }},
                    boxShadow: {{ 'glow': '0 0 40px -10px rgba(153, 27, 27, 0.4)' }}
                }}
            }}
        }}
    </script>
</head>
<body class="font-body bg-dark text-slate-300 antialiased selection:bg-primary selection:text-white min-h-screen flex flex-col">
    <nav class="fixed w-full top-0 z-50 bg-dark/95 backdrop-blur-lg border-b border-white/5 h-16 sm:h-20 flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full flex justify-between items-center">
            <a href="index.html" class="font-heading font-bold text-xl sm:text-2xl tracking-widest text-white uppercase">
                WARAX<span class="text-primary">GAMING</span>
            </a>
            <div class="flex items-center gap-4 sm:gap-6">
                <a href="index.html" class="text-slate-400 hover:text-white text-xs sm:text-sm font-semibold uppercase tracking-wider flex items-center gap-2">
                    <i class="fa-solid fa-arrow-left"></i> <span class="hidden sm:inline">Main Store</span>
                </a>
                <button onclick="openPayUCheckout()" class="text-slate-400 hover:text-white relative p-2">
                    <i class="fa-solid fa-cart-shopping text-lg"></i>
                    <span id="cart-count-badge" class="absolute top-0 right-0 bg-primary text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full border border-dark">0</span>
                </button>
            </div>
        </div>
    </nav>
    <main class="pt-24 sm:pt-32 pb-16 flex-grow">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center gap-2 text-[11px] text-slate-500 mb-8 flex-wrap">
                <a href="index.html" class="hover:text-white">Store</a>
                <span>/</span>
                <span class="text-slate-400">{category}</span>
                <span>/</span>
                <span class="text-white font-semibold">{name}</span>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 sm:gap-16 items-start">
                <div class="space-y-4">
                    <div class="bg-surface border border-white/10 rounded-2xl overflow-hidden aspect-square relative flex items-center justify-center p-4">
                        <img src="{img_src}" alt="{name}" class="w-full h-full object-contain">
                        {f'<div class="absolute top-4 left-4 bg-primary text-white font-heading font-bold text-sm px-3 py-1.5 rounded-lg">{discount}% OFF</div>' if discount > 0 else ''}
                    </div>
                </div>
                <div class="space-y-6">
                    <div>
                        <span class="text-primary font-bold text-[11px] uppercase tracking-widest">{brand} • {category}</span>
                        <h1 class="font-heading font-extrabold text-3xl sm:text-4xl text-white mt-1 tracking-tight leading-tight">{name}</h1>
                    </div>
                    <div class="bg-surface border border-white/10 rounded-2xl p-6 space-y-3">
                        <div class="flex items-end gap-4 flex-wrap">
                            <span class="font-heading font-black text-4xl sm:text-5xl text-white">₹{price:,}</span>
                            {f'''<div class="flex flex-col"><span class="text-slate-500 line-through text-lg">₹{original_price:,}</span><span class="text-green-400 font-bold text-sm">You Save ₹{savings:,} ({discount}% OFF)</span></div>''' if original_price > price else ''}
                        </div>
                        <p class="text-[11px] text-slate-500">Inclusive of all taxes. Free delivery across India via PayU Secure Checkout.</p>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-4">
                        <button onclick="addToCart({pid})" class="flex-1 min-h-[52px] bg-primary hover:bg-primaryHover text-white font-bold text-xs uppercase tracking-widest rounded-xl flex items-center justify-center gap-3">
                            <i class="fa-solid fa-cart-plus text-base"></i> Add to Cart
                        </button>
                        <button onclick="addToCart({pid}, false); openPayUCheckout();" class="flex-1 min-h-[52px] border border-white/20 hover:border-primary text-white font-bold text-xs uppercase tracking-widest rounded-xl flex items-center justify-center gap-3">
                            <i class="fa-solid fa-shield-halved text-base text-green-500"></i> Buy Now (PayU)
                        </button>
                    </div>
                    {specs_html}
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-dark text-slate-400 py-10 border-t border-white/5 text-center text-xs">
        <p>&copy; 2026 WARAX GAMING • All Rights Reserved</p>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <script src="products.js"></script>
    <script src="payu-checkout.js"></script>
</body>
</html>"""

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        count += 1

    print(f"OK: Generated {count} product HTML pages (product-1.html to product-{count}.html)!")

if __name__ == '__main__':
    build_all()
