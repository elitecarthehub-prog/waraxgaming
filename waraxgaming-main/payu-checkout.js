/**
 * WARAX GAMING — Store Cart & Checkout Integration Script
 */

let cart = JSON.parse(localStorage.getItem('warax_cart')) || [];

function saveCart() {
    localStorage.setItem('warax_cart', JSON.stringify(cart));
    updateCartBadges();
}

function updateCartBadges() {
    const totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
    document.querySelectorAll('.cart-count-badge').forEach(badge => {
        badge.innerText = totalCount;
    });
}

function addToCart(productId, openDrawer = true) {
    if (typeof PRODUCTS_DATA === 'undefined') return;
    const p = PRODUCTS_DATA.find(item => item.id === productId);
    if (!p) return;

    const existing = cart.find(item => item.id === productId);
    if (existing) {
        existing.qty += 1;
    } else {
        cart.push({
            id: p.id,
            name: p.name,
            price: p.price,
            originalPrice: p.originalPrice || p.price,
            discount: p.discount || 0,
            image: p.image,
            brand: p.brand || 'WARAX',
            qty: 1
        });
    }
    saveCart();

    if (openDrawer) {
        openCartDrawer();
    }
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    saveCart();
    renderCartDrawer();
}

function updateQty(productId, delta) {
    const item = cart.find(i => i.id === productId);
    if (item) {
        item.qty += delta;
        if (item.qty <= 0) {
            removeFromCart(productId);
        } else {
            saveCart();
            renderCartDrawer();
        }
    }
}

function openPayUCheckout() {
    openCartDrawer();
}

function openCartDrawer() {
    let modal = document.getElementById('cart-drawer-modal');
    if (!modal) {
        createCartModal();
        modal = document.getElementById('cart-drawer-modal');
    }
    renderCartDrawer();
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeCartDrawer() {
    const modal = document.getElementById('cart-drawer-modal');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

function closePayUCheckout() {
    closeCartDrawer();
}

function createCartModal() {
    const modalHtml = `
    <div id="cart-drawer-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-sm flex justify-end">
        <div class="w-full max-w-md bg-surface border-l border-white/10 h-full flex flex-col justify-between shadow-2xl relative">
            
            <!-- Drawer Header -->
            <div class="px-6 py-5 border-b border-white/10 flex items-center justify-between bg-dark">
                <div class="flex items-center gap-3">
                    <i class="fa-solid fa-cart-shopping text-primary text-xl"></i>
                    <div>
                        <h3 class="font-heading font-black text-white text-base tracking-wide uppercase">Your Shopping Cart</h3>
                        <span class="text-[10px] text-green-400 font-bold tracking-widest uppercase flex items-center gap-1">
                            <i class="fa-solid fa-truck-fast"></i> FREE Express Delivery Across India
                        </span>
                    </div>
                </div>
                <button onclick="closeCartDrawer()" class="text-slate-400 hover:text-white text-lg p-2">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Drawer Items List -->
            <div class="p-6 overflow-y-auto space-y-4 flex-grow" id="cart-drawer-items">
                <!-- Populated dynamically -->
            </div>

            <!-- Drawer Footer -->
            <div class="p-6 border-t border-white/10 bg-dark space-y-4">
                <div class="space-y-1.5 text-xs">
                    <div class="flex justify-between text-slate-400">
                        <span>Original Subtotal</span>
                        <span id="drawer-subtotal">₹0</span>
                    </div>
                    <div class="flex justify-between text-green-400 font-bold">
                        <span>Discount Savings</span>
                        <span id="drawer-savings">-₹0</span>
                    </div>
                    <div class="flex justify-between text-slate-400">
                        <span>Delivery</span>
                        <span class="text-green-400 font-bold">FREE</span>
                    </div>
                    <div class="flex justify-between text-white font-black text-base pt-2 border-t border-white/5">
                        <span>Total Payable</span>
                        <span id="drawer-grandtotal" class="text-primary">₹0</span>
                    </div>
                </div>

                <a href="checkout.html" class="w-full py-4 bg-primary hover:bg-primaryHover text-white font-bold text-xs uppercase tracking-widest rounded-xl flex items-center justify-center gap-2 shadow-glow transition no-underline">
                    <i class="fa-solid fa-lock text-sm"></i> Proceed to Checkout (FREE Delivery)
                </a>
            </div>

        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);
}

function renderCartDrawer() {
    const container = document.getElementById('cart-drawer-items');
    if (!container) return;

    if (cart.length === 0) {
        container.innerHTML = `
            <div class="text-center py-12 text-slate-500 space-y-3">
                <i class="fa-solid fa-cart-shopping text-4xl mb-1"></i>
                <p class="text-xs font-semibold">Your shopping cart is empty.</p>
                <button onclick="closeCartDrawer()" class="px-5 py-2.5 bg-primary text-white text-xs font-bold uppercase rounded-lg">Explore Store</button>
            </div>
        `;
        document.getElementById('drawer-subtotal').innerText = '₹0';
        document.getElementById('drawer-savings').innerText = '-₹0';
        document.getElementById('drawer-grandtotal').innerText = '₹0';
        return;
    }

    let subtotal = 0;
    let originalTotal = 0;

    container.innerHTML = cart.map(item => {
        const itemOrig = (item.originalPrice || item.price) * item.qty;
        const itemSale = item.price * item.qty;
        subtotal += itemSale;
        originalTotal += itemOrig;

        return `
            <div class="flex items-center gap-3 p-3 bg-dark border border-white/5 rounded-xl">
                <img src="${item.image}" alt="${item.name}" class="w-14 h-14 object-contain rounded-lg bg-surface p-1">
                <div class="flex-grow min-w-0">
                    <h5 class="font-heading font-bold text-white text-xs truncate">${item.name}</h5>
                    <div class="flex items-center gap-2 mt-1">
                        <span class="font-heading font-bold text-sm text-white">₹${(item.price * item.qty).toLocaleString('en-IN')}</span>
                        ${item.originalPrice > item.price ? `<span class="text-[10px] text-slate-500 line-through">₹${(item.originalPrice * item.qty).toLocaleString('en-IN')}</span>` : ''}
                    </div>
                </div>
                <div class="flex items-center gap-1 bg-surface border border-white/10 rounded-lg p-1">
                    <button onclick="updateQty(${item.id}, -1)" class="w-6 h-6 text-slate-400 hover:text-white text-xs flex items-center justify-center">-</button>
                    <span class="text-xs font-bold text-white px-2">${item.qty}</span>
                    <button onclick="updateQty(${item.id}, 1)" class="w-6 h-6 text-slate-400 hover:text-white text-xs flex items-center justify-center">+</button>
                </div>
            </div>
        `;
    }).join('');

    const savings = originalTotal - subtotal;
    document.getElementById('drawer-subtotal').innerText = `₹${originalTotal.toLocaleString('en-IN')}`;
    document.getElementById('drawer-savings').innerText = `-₹${savings.toLocaleString('en-IN')}`;
    document.getElementById('drawer-grandtotal').innerText = `₹${subtotal.toLocaleString('en-IN')}`;
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartBadges();
});
