import os
import re

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"

# 1. FIX CONSOLES.HTML
consoles_path = os.path.join(ROOT, "consoles.html")
with open(consoles_path, 'r', encoding='utf-8') as f:
    c_txt = f.read()

old_c_card = """grid.innerHTML = filtered.map(item => `
                <div class="bg-surface border border-white/5 hover-lift flex flex-col group p-5 rounded-xl">"""

new_c_card = """grid.innerHTML = filtered.map(item => `
                <div class="bg-surface border border-white/5 hover-lift flex flex-col group p-5 rounded-xl cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

if old_c_card in c_txt:
    c_txt = c_txt.replace(old_c_card, new_c_card)
    with open(consoles_path, 'w', encoding='utf-8') as f:
        f.write(c_txt)
    print("OK: Fixed consoles.html card onclick link!")
else:
    print("Consoles.html card already has onclick link or pattern different.")

# 2. FIX CONTROLLERS.HTML
controllers_path = os.path.join(ROOT, "controllers.html")
with open(controllers_path, 'r', encoding='utf-8') as f:
    ctrl_txt = f.read()

old_ctrl_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between">"""

new_ctrl_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

if old_ctrl_card in ctrl_txt:
    ctrl_txt = ctrl_txt.replace(old_ctrl_card, new_ctrl_card)
    with open(controllers_path, 'w', encoding='utf-8') as f:
        f.write(ctrl_txt)
    print("OK: Fixed controllers.html card onclick link!")

# 3. FIX HEADSETS.HTML
headsets_path = os.path.join(ROOT, "headsets.html")
with open(headsets_path, 'r', encoding='utf-8') as f:
    h_txt = f.read()

old_h_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between">"""

new_h_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

if old_h_card in h_txt:
    h_txt = h_txt.replace(old_h_card, new_h_card)
    with open(headsets_path, 'w', encoding='utf-8') as f:
        f.write(h_txt)
    print("OK: Fixed headsets.html card onclick link!")

# 4. FIX HARDWARE.HTML
hardware_path = os.path.join(ROOT, "hardware.html")
with open(hardware_path, 'r', encoding='utf-8') as f:
    hw_txt = f.read()

old_hw_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between">"""

new_hw_card = """grid.innerHTML = list.map(item => `
                <div class="bg-surface border border-white/5 hover-lift p-5 rounded-xl flex flex-col justify-between cursor-pointer" onclick="window.location.href='product-' + item.id + '.html'">"""

if old_hw_card in hw_txt:
    hw_txt = hw_txt.replace(old_hw_card, new_hw_card)
    with open(hardware_path, 'w', encoding='utf-8') as f:
        f.write(hw_txt)
    print("OK: Fixed hardware.html card onclick link!")

# 5. FIX GAMES.HTML
games_path = os.path.join(ROOT, "games.html")
with open(games_path, 'r', encoding='utf-8') as f:
    g_txt = f.read()

old_g_card = """<a href="product.html?id=${item.id}" class="bg-surface border border-white/5 hover-lift rounded-xl overflow-hidden flex flex-col group">"""
new_g_card = """<a href="product-${item.id}.html" class="bg-surface border border-white/5 hover-lift rounded-xl overflow-hidden flex flex-col group">"""

if old_g_card in g_txt:
    g_txt = g_txt.replace(old_g_card, new_g_card)
    with open(games_path, 'w', encoding='utf-8') as f:
        f.write(g_txt)
    print("OK: Fixed games.html card onclick link!")

print("All catalog pages checked and updated!")
