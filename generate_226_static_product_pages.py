import json
import os
import re

PRODUCTS_JS = r"c:\Users\arthe\Downloads\New folder (3)\products.js"
PRODUCTS_DIR = r"c:\Users\arthe\Downloads\New folder (3)\products"

os.makedirs(PRODUCTS_DIR, exist_ok=True)

with open(PRODUCTS_JS, 'r', encoding='utf-8') as f:
    txt = f.read()

products = json.loads(txt.replace("const PRODUCTS_DATA = ", "").rstrip(";\n"))

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def build_specs_html(p):
    rows = []
    if p.get('brand'): rows.append(('Brand', p['brand']))
    if p.get('sheetCategory'): rows.append(('Category', p['sheetCategory']))
    if p.get('compatibility'): rows.append(('Compatibility', p['compatibility']))
    
    cat = p.get('sheetCategory', '')
    if cat == 'Consoles':
        rows.append(('Generation', p.get('generation') or 'Current / Next-Gen'))
        rows.append(('Storage', '825GB – 2TB SSD'))
        rows.append(('Resolution', '4K / 8K Ultra HD'))
        rows.append(('Frame Rate', 'Up to 120fps'))
    elif cat == 'Controllers':
        rows.append(('Connection', 'Wireless + USB-C Cable'))
        rows.append(('Battery', '12–40 hours'))
        rows.append(('Haptics', 'Advanced Haptic Feedback'))
    elif cat == 'Headsets':
        rows.append(('Type', 'Over-Ear Wireless Gaming'))
        rows.append(('Driver', '40mm Neodymium Drivers'))
        rows.append(('Frequency', '20Hz – 20kHz'))
        rows.append(('Battery Life', 'Up to 30 hours'))
    elif cat == 'VR':
        rows.append(('Display', 'OLED / LCD Pancake Lenses'))
        rows.append(('Refresh Rate', '90–120Hz'))
        rows.append(('Tracking', '6-DOF Inside-Out'))
    elif cat == 'Storage':
        rows.append(('Interface', 'M.2 NVMe PCIe 4.0 / MicroSD'))
        rows.append(('Read Speed', 'Up to 7000 MB/s'))
    elif cat == 'Monitors':
        rows.append(('Panel', 'OLED / IPS Gaming Panel'))
        rows.append(('Refresh Rate', '144–360Hz'))
        rows.append(('Response Time', '0.1 – 1ms GTG'))

    if p.get('originalPrice'): rows.append(('Original MRP', f"₹{p['originalPrice']:,}"))
    if p.get('discount'): rows.append(('Discount', f"{p['discount']}% Off (WARAX Deal)"))

    if not rows:
        return ''

    rows_html = "".join([f"""
        <div class="flex justify-between items-start px-5 py-3 text-xs border-b border-white/5">
            <span class="text-slate-400 font-semibold w-1/3">{label}</span>
            <span class="text-white w-2/3 text-right">{val}</span>
        </div>
    """ for label, val in rows])

    return f"""
    <div class="border border-white/10 rounded-2xl overflow-hidden mt-6">
        <div class="bg-surface px-5 py-3 border-b border-white/10">
            <h3 class="font-heading font-bold text-white text-sm uppercase tracking-wider">Product Specifications</h3>
        </div>
        <div class="divide-y divide-white/5">
            {rows_html}
        </div>
    </div>
    """

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
    img_src = p.get('image', '')
    if img_src.startswith('images/'):
        img_src = "../" + img_src

    slug = slugify(name)
    file_path = os.path.join(PRODUCTS_DIR, f"product-{pid}.html")
    slug_file_path = os.path.join(PRODUCTS_DIR, f"{slug}.html")

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
    <style>
        html {{ scroll-behavior: smooth; }}
        .hover-lift {{ transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1); }}
        .hover-lift:hover {{ transform: translateY(-4px); }}
        .btn-anim {{ transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }}
        .btn-anim:active {{ transform: scale(0.96); }}
        .badge-pulse {{ animation: badgePulse 2s ease-in-out infinite; }}
        @keyframes badgePulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.7; }} }}
    </style>
</head>
<body class="font-body bg-dark text-slate-300 antialiased selection:bg-primary selection:text-white min-h-screen flex flex-col">

    <!-- Navbar -->
    <nav class="fixed w-full top-0 z-50 bg-dark/95 backdrop-blur-lg border-b border-white/5 h-16 sm:h-20 flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full flex justify-between items-center">
            <a href="../index.html" class="font-heading font-bold text-xl sm:text-2xl tracking-widest text-white uppercase">
                WARAX<span class="text-primary">GAMING</span>
            </a>
            <div class="flex items-center gap-4 sm:gap-6">
                <a href="../index.html" class="text-slate-400 hover:text-white text-xs sm:text-sm font-semibold uppercase tracking-wider flex items-center gap-2">
                    <i class="fa-solid fa-arrow-left"></i> <span class="hidden sm:inline">Main Store</span>
                </a>
                <button onclick="openPayUCheckout()" class="text-slate-400 hover:text-white relative p-2">
                    <i class="fa-solid fa-cart-shopping text-lg"></i>
                    <span id="cart-count-badge" class="absolute top-0 right-0 bg-primary text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full border border-dark">0</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Product Content -->
    <main class="pt-24 sm:pt-32 pb-16 flex-grow">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Breadcrumb -->
            <div class="flex items-center gap-2 text-[11px] text-slate-500 mb-8 flex-wrap">
                <a href="../index.html" class="hover:text-white">Store</a>
                <span>/</span>
                <span class="text-slate-400">{category}</span>
                <span>/</span>
                <span class="text-white font-semibold">{name}</span>
            </div>

            <!-- Product Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 sm:gap-16 items-start">

                <!-- Left: Image -->
                <div class="space-y-4">
                    <div class="bg-surface border border-white/10 rounded-2xl overflow-hidden aspect-square relative flex items-center justify-center p-4">
                        <img src="{img_src}" alt="{name}" class="w-full h-full object-contain">
                        {f'<div class="absolute top-4 left-4 bg-primary text-white font-heading font-bold text-sm px-3 py-1.5 rounded-lg badge-pulse">{discount}% OFF</div>' if discount > 0 else ''}
                        <div class="absolute top-4 right-4 bg-white/10 border border-white/20 text-white font-semibold text-[10px] px-2.5 py-1 rounded uppercase tracking-wider backdrop-blur-sm">Genuine Stock</div>
                    </div>
                    <!-- Trust Badges -->
                    <div class="grid grid-cols-3 gap-3 text-center">
                        <div class="bg-surface border border-white/5 rounded-xl p-3">
                            <i class="fa-solid fa-truck-fast text-primary text-lg mb-1"></i>
                            <p class="text-[10px] font-semibold text-white uppercase">Free Delivery</p>
                            <p class="text-[9px] text-slate-500">All India</p>
                        </div>
                        <div class="bg-surface border border-white/5 rounded-xl p-3">
                            <i class="fa-solid fa-shield-halved text-primary text-lg mb-1"></i>
                            <p class="text-[10px] font-semibold text-white uppercase">Genuine</p>
                            <p class="text-[9px] text-slate-500">Official Stock</p>
                        </div>
                        <div class="bg-surface border border-white/5 rounded-xl p-3">
                            <i class="fa-solid fa-rotate-left text-primary text-lg mb-1"></i>
                            <p class="text-[10px] font-semibold text-white uppercase">7-Day Return</p>
                            <p class="text-[9px] text-slate-500">Easy Process</p>
                        </div>
                    </div>
                </div>

                <!-- Right: Info -->
                <div class="space-y-6">
                    <div>
                        <span class="text-primary font-bold text-[11px] uppercase tracking-widest">{brand} • {category}</span>
                        <h1 class="font-heading font-extrabold text-3xl sm:text-4xl text-white mt-1 tracking-tight leading-tight">{name}</h1>
                        {f'<p class="text-slate-400 text-sm mt-2">Compatible with: <span class="text-white font-semibold">{p["compatibility"]}</span></p>' if p.get("compatibility") else ''}
                    </div>

                    <!-- Rating -->
                    <div class="flex items-center gap-3">
                        <div class="flex text-primary text-sm">
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star-half-stroke"></i>
                        </div>
                        <span class="text-slate-400 text-xs">4.8 / 5 • Highly Rated by Gamers</span>
                    </div>

                    <!-- Price Block -->
                    <div class="bg-surface border border-white/10 rounded-2xl p-6 space-y-3">
                        <div class="flex items-end gap-4 flex-wrap">
                            <span class="font-heading font-black text-4xl sm:text-5xl text-white">₹{price:,}</span>
                            {f'''<div class="flex flex-col">
                                <span class="text-slate-500 line-through text-lg">₹{original_price:,}</span>
                                <span class="text-green-400 font-bold text-sm">You Save ₹{savings:,} ({discount}% OFF)</span>
                            </div>''' if original_price > price else ''}
                        </div>
                        <p class="text-[11px] text-slate-500">Inclusive of all taxes. Free delivery across India via PayU Secure Checkout.</p>
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-green-400 inline-block animate-pulse"></span>
                            <span class="text-green-400 text-xs font-semibold">In Stock — Ready to Dispatch</span>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex flex-col sm:flex-row gap-4">
                        <button onclick="addToCart({pid})" class="btn-anim flex-1 min-h-[52px] bg-primary hover:bg-primaryHover text-white font-bold text-xs uppercase tracking-widest rounded-xl flex items-center justify-center gap-3 shadow-glow">
                            <i class="fa-solid fa-cart-plus text-base"></i>
                            Add to Cart
                        </button>
                        <button onclick="addToCart({pid}, false); openPayUCheckout();" class="btn-anim flex-1 min-h-[52px] border border-white/20 hover:border-primary hover:text-primary text-white font-bold text-xs uppercase tracking-widest rounded-xl flex items-center justify-center gap-3">
                            <i class="fa-solid fa-shield-halved text-base text-green-500"></i>
                            Buy Now (PayU)
                        </button>
                    </div>

                    <!-- Specs -->
                    {build_specs_html(p)}

                    <!-- Description -->
                    {f'''<div class="bg-surface/50 border border-white/10 rounded-2xl p-5">
                        <h3 class="font-heading font-bold text-white text-sm uppercase tracking-wider mb-2">Product Description</h3>
                        <p class="text-slate-400 text-xs leading-relaxed">{p["description"]}</p>
                    </div>''' if p.get("description") else ''}

                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-dark text-slate-400 py-10 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs">
            <span class="font-heading font-bold text-white uppercase tracking-widest">WARAX<span class="text-primary">GAMING</span></span>
            <span>&copy; 2026 WARAX GAMING. All rights reserved.</span>
            <a href="../index.html" class="text-primary font-semibold uppercase">Main Store &rarr;</a>
        </div>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <script src="../products.js"></script>
    <script src="../payu-checkout.js"></script>
</body>
</html>"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    if slug:
        with open(slug_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

    count += 1

print(f"Successfully generated {count} individual static product HTML pages in 'products/' directory!")
