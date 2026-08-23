import os
import shutil

ROOT = r"c:\Users\arthe\Downloads\New folder (3)"
BACKEND = r"c:\Users\arthe\Downloads\elitecart-backend-main\elitecart-backend-main"

# Copy api folder
api_src = os.path.join(BACKEND, "api")
api_dst = os.path.join(ROOT, "api")
if os.path.exists(api_dst):
    shutil.rmtree(api_dst)
shutil.copytree(api_src, api_dst)
print("Copied api/ directory to root project!")

# Copy lib folder
lib_src = os.path.join(BACKEND, "lib")
lib_dst = os.path.join(ROOT, "lib")
if os.path.exists(lib_dst):
    shutil.rmtree(lib_dst)
shutil.copytree(lib_src, lib_dst)
print("Copied lib/ directory to root project!")

# Copy vercel.json
shutil.copy(os.path.join(BACKEND, "vercel.json"), os.path.join(ROOT, "vercel.json"))
print("Copied vercel.json to root project!")

# Copy package.json
shutil.copy(os.path.join(BACKEND, "package.json"), os.path.join(ROOT, "package.json"))
print("Copied package.json to root project!")
