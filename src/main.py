import os
import shutil
from copystatic import copy_directory_recursive
from generate_page import generate_pages_recursive # <-- Updated import statement

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_DIR = os.path.join(BASE_DIR, "static")
DST_DIR = os.path.join(BASE_DIR, "public")
CONTENT_DIR = os.path.join(BASE_DIR, "content") # <-- Points to the whole directory now
TEMPLATE_FILE = os.path.join(BASE_DIR, "template.html")

def main():
    print("Initializing static site generation build pipeline...")
    
    # 1. Clean and reset the destination directory
    if os.path.exists(DST_DIR):
        print(f"Wiping existing build contents at: {DST_DIR}")
        shutil.rmtree(DST_DIR)
        
    print(f"Re-initializing empty public container at: {DST_DIR}")
    os.mkdir(DST_DIR)
    
    # 2. Trigger the asset copy loop
    if os.path.exists(SRC_DIR):
        print(f"Beginning asset copying loop from '{SRC_DIR}' to '{DST_DIR}'...")
        copy_directory_recursive(SRC_DIR, DST_DIR)
    
    # 3. Recursively compile ALL markdown contents down to the public directory tree
    print(f"Building HTML files recursively from {CONTENT_DIR}...")
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_FILE, DST_DIR)
    
    print("Full site architecture build pipeline completed successfully!")

if __name__ == "__main__":
    main()
