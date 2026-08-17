import os
import re

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"

def fix_consoles():
    path = os.path.join(ROOT, "consoles.html")
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    # Replace div card with a card
    old_code = """            grid.innerHTML = filtered.map(item => `
                <div class="bg-surface border border-white/5 hover-lift flex flex-col group p-5 rounded-xl cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""
    
    new_code = """            grid.innerHTML = filtered.map(item => `
                <a href="product-${item.id}.html" class="bg-surface border border-white/5 hover-lift flex flex-col group p-5 rounded-xl text-left no-underline block">"""

    txt = txt.replace(old_code, new_code)
    
    # Fix button inside a tag
    txt = txt.replace("onclick=\"event.stopPropagation(); addToCart(${item.id})\"", "onclick=\"event.preventDefault(); event.stopPropagation(); addToCart(${item.id})\"")
    # Replace closing </div> for card with </a>
    # Note: the card closes right before .join('')
    txt = re.sub(r'(addToCart\(\$\{item\.id\}\)"[^>]*>.*?<\/button>\s*<\/div>\s*<\/div>\s*)(<\/div>)(\s*\`\)\.join)', r'\1</a>\3', txt, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Fixed consoles.html to use native <a> links")

def fix_controllers():
    path = os.path.join(ROOT, "controllers.html")
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    old_code = """            grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

    new_code = """            grid.innerHTML = list.map(item => `
                <a href="product-${item.id}.html" class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between text-left no-underline block">"""

    txt = txt.replace(old_code, new_code)
    txt = txt.replace("onclick=\"event.stopPropagation(); addToCart(${item.id})\"", "onclick=\"event.preventDefault(); event.stopPropagation(); addToCart(${item.id})\"")
    txt = re.sub(r'(addToCart\(\$\{item\.id\}\)"[^>]*>.*?<\/button>\s*<\/div>\s*)(<\/div>)(\s*\`\)\.join)', r'\1</a>\3', txt, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Fixed controllers.html to use native <a> links")

def fix_headsets():
    path = os.path.join(ROOT, "headsets.html")
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    old_code = """            grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

    new_code = """            grid.innerHTML = list.map(item => `
                <a href="product-${item.id}.html" class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between text-left no-underline block">"""

    txt = txt.replace(old_code, new_code)
    txt = txt.replace("onclick=\"event.stopPropagation(); addToCart(${item.id})\"", "onclick=\"event.preventDefault(); event.stopPropagation(); addToCart(${item.id})\"")
    txt = re.sub(r'(addToCart\(\$\{item\.id\}\)"[^>]*>.*?<\/button>\s*<\/div>\s*)(<\/div>)(\s*\`\)\.join)', r'\1</a>\3', txt, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Fixed headsets.html to use native <a> links")

def fix_hardware():
    path = os.path.join(ROOT, "hardware.html")
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    old_code = """            grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

    new_code = """            grid.innerHTML = list.map(item => `
                <a href="product-${item.id}.html" class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between text-left no-underline block">"""

    txt = txt.replace(old_code, new_code)
    txt = txt.replace("onclick=\"event.stopPropagation(); addToCart(${item.id})\"", "onclick=\"event.preventDefault(); event.stopPropagation(); addToCart(${item.id})\"")
    txt = re.sub(r'(addToCart\(\$\{item\.id\}\)"[^>]*>.*?<\/button>\s*<\/div>\s*)(<\/div>)(\s*\`\)\.join)', r'\1</a>\3', txt, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Fixed hardware.html to use native <a> links")

def fix_index():
    path = os.path.join(ROOT, "index.html")
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    txt = txt.replace("onclick=\"window.location.href='product-${item.id}.html'\"", "")
    # Replace div cards with <a href="product-${item.id}.html">
    txt = txt.replace("<div class=\"snap-center shrink-0 w-[85vw] sm:w-auto bg-surface border border-white/5 hover-lift flex flex-col group p-5 sm:p-6 rounded-xl cursor-pointer\"", "<a href=\"product-${item.id}.html\" class=\"snap-center shrink-0 w-[85vw] sm:w-auto bg-surface border border-white/5 hover-lift flex flex-col group p-5 sm:p-6 rounded-xl block text-left no-underline\"")
    txt = txt.replace("<div class=\"bg-dark border border-white/5 p-4 hover-lift group rounded-xl flex flex-col justify-between cursor-pointer\"", "<a href=\"product-${item.id}.html\" class=\"bg-dark border border-white/5 p-4 hover-lift group rounded-xl flex flex-col justify-between block text-left no-underline\"")
    txt = txt.replace("onclick=\"addToCart(${item.id})\"", "onclick=\"event.preventDefault(); event.stopPropagation(); addToCart(${item.id})\"")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Fixed index.html to use native <a> links")

fix_consoles()
fix_controllers()
fix_headsets()
fix_hardware()
fix_index()
print("All pages converted to native HTML <a> links!")
