import os
import re

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"

FOOTER_HTML = """    <!-- PREMIUM FOOTER -->
    <footer class="bg-dark text-slate-400 border-t border-white/10 pt-16 pb-8 no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
            
            <!-- Top Footer Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 sm:gap-10">
                
                <!-- Col 1: Brand Info & Subsidiary Tag -->
                <div class="lg:col-span-2 space-y-4">
                    <div class="flex items-center gap-2">
                        <a href="index.html" class="font-heading font-black text-2xl tracking-widest text-white uppercase">
                            WARAX<span class="text-primary">GAMING</span>
                        </a>
                    </div>
                    
                    <!-- Daughter Company / Subsidiary Badge -->
                    <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary/10 border border-primary/30 rounded-lg text-primary text-xs font-bold uppercase tracking-wider">
                        <i class="fa-solid fa-building-shield"></i> A Subsidiary of ELITE CART
                    </div>

                    <p class="text-xs text-slate-400 leading-relaxed max-w-sm">
                        India’s premier gaming destination since 2017. Supplying 100% genuine gaming consoles, physical disc titles, wireless controllers, VR headsets, and high-performance hardware.
                    </p>

                    <!-- Trust Badges -->
                    <div class="flex items-center gap-4 text-xs font-bold text-slate-300 pt-2">
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-halved text-green-400"></i> 100% Genuine</span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-truck-fast text-primary"></i> Free Express Shipping</span>
                    </div>
                </div>

                <!-- Col 2: Store Categories -->
                <div class="space-y-3">
                    <h4 class="font-heading font-bold text-white text-xs uppercase tracking-widest border-b border-primary/40 pb-2 inline-block">Store Categories</h4>
                    <ul class="space-y-2 text-xs">
                        <li><a href="consoles.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Gaming Consoles</a></li>
                        <li><a href="games.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Video Game Discs</a></li>
                        <li><a href="controllers.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Wireless Controllers</a></li>
                        <li><a href="headsets.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Headsets & VR</a></li>
                        <li><a href="hardware.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Hardware & Accessories</a></li>
                    </ul>
                </div>

                <!-- Col 3: Customer Care & Links -->
                <div class="space-y-3">
                    <h4 class="font-heading font-bold text-white text-xs uppercase tracking-widest border-b border-primary/40 pb-2 inline-block">Customer Care</h4>
                    <ul class="space-y-2 text-xs">
                        <li><a href="track.html" class="text-green-400 font-bold hover:text-green-300 transition flex items-center gap-1.5"><i class="fa-solid fa-truck-fast text-[10px]"></i> Track Order Live</a></li>
                        <li><a href="checkout.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Express Checkout</a></li>
                        <li><a href="index.html#accessories-section" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-chevron-right text-[10px] text-slate-600"></i> Featured Accessories</a></li>
                        <li><a href="admin.html" class="hover:text-primary transition flex items-center gap-1.5"><i class="fa-solid fa-lock text-[10px] text-slate-600"></i> Admin Portal</a></li>
                    </ul>
                </div>

                <!-- Col 4: Store Location & Address -->
                <div class="space-y-3">
                    <h4 class="font-heading font-bold text-white text-xs uppercase tracking-widest border-b border-primary/40 pb-2 inline-block">Head Office & Store</h4>
                    <div class="space-y-2.5 text-xs text-slate-400">
                        <p class="flex items-start gap-2">
                            <i class="fa-solid fa-location-dot text-primary mt-0.5 text-sm"></i>
                            <span><strong>WARAX GAMING</strong><br>A Division of ELITE CART Retail Pvt. Ltd.<br>Shop No. 104, 1st Floor, Building 88, Nehru Place, New Delhi - 110019</span>
                        </p>
                        <p class="flex items-center gap-2">
                            <i class="fa-solid fa-envelope text-primary text-sm"></i>
                            <a href="mailto:support@waraxgaming.store" class="hover:text-white">support@waraxgaming.store</a>
                        </p>
                        <p class="flex items-center gap-2">
                            <i class="fa-solid fa-clock text-green-400 text-sm"></i>
                            <span>Mon - Sat: 10:00 AM - 8:00 PM IST</span>
                        </p>
                    </div>
                </div>

            </div>

            <!-- Bottom Divider & Payment Icons -->
            <div class="border-t border-white/10 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs">
                <div class="space-y-1 text-center sm:text-left">
                    <p class="text-slate-400 font-medium">&copy; 2017 - 2026 <strong>WARAX GAMING</strong> • All Rights Reserved.</p>
                    <p class="text-[11px] text-slate-500">WARAX GAMING is an Official Sub-Brand & Subsidiary Entity of <strong>ELITE CART</strong>.</p>
                </div>

                <!-- Payment Methods Badges -->
                <div class="flex flex-wrap items-center justify-center gap-2 text-[10px] font-bold text-slate-400">
                    <span class="bg-surface px-2.5 py-1 rounded-md border border-white/10 text-white"><i class="fa-solid fa-qrcode text-green-400 mr-1"></i> UPI</span>
                    <span class="bg-surface px-2.5 py-1 rounded-md border border-white/10 text-white"><i class="fa-brands fa-cc-visa text-blue-400 mr-1"></i> VISA</span>
                    <span class="bg-surface px-2.5 py-1 rounded-md border border-white/10 text-white"><i class="fa-brands fa-cc-mastercard text-red-400 mr-1"></i> MASTERCARD</span>
                    <span class="bg-surface px-2.5 py-1 rounded-md border border-white/10 text-white">RUPAY</span>
                    <span class="bg-surface px-2.5 py-1 rounded-md border border-white/10 text-white"><i class="fa-solid fa-lock text-green-400 mr-1"></i> 256-BIT SSL</span>
                </div>
            </div>

        </div>
    </footer>"""

def update_footer(file_path, is_subfolder=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace existing footer block
    content = re.sub(r'<footer.*?>.*?</footer>', FOOTER_HTML, content, flags=re.DOTALL)
    
    if is_subfolder:
        # Fix relative links for products/*.html subfolder
        content = content.replace('href="index.html', 'href="../index.html')
        content = content.replace('href="consoles.html', 'href="../consoles.html')
        content = content.replace('href="games.html', 'href="../games.html')
        content = content.replace('href="controllers.html', 'href="../controllers.html')
        content = content.replace('href="headsets.html', 'href="../headsets.html')
        content = content.replace('href="hardware.html', 'href="../hardware.html')
        content = content.replace('href="checkout.html', 'href="../checkout.html')
        content = content.replace('href="track.html', 'href="../track.html')
        content = content.replace('href="admin.html', 'href="../admin.html')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Root HTML files
root_htmls = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.html')]
for file_path in root_htmls:
    update_footer(file_path, is_subfolder=False)
    print(f"Updated footer in: {os.path.basename(file_path)}")

# Update Subfolder products/*.html files
products_dir = os.path.join(ROOT, "products")
if os.path.exists(products_dir):
    p_files = [os.path.join(products_dir, f) for f in os.listdir(products_dir) if f.endswith('.html')]
    for file_path in p_files:
        update_footer(file_path, is_subfolder=True)
    print(f"Updated footer in {len(p_files)} product pages in products/")

print("OK: Premium Footer updated across all website pages!")
