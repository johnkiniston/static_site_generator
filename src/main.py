import os
import sys
import shutil
from copystatic import copy_directory_recursive
from generate_page import generate_pages_recursive

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_DIR = os.path.join(BASE_DIR, "static")
DST_DIR = os.path.join(BASE_DIR, "docs")
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATE_FILE = os.path.join(BASE_DIR, "template.html")

def main():
    # Capture command line arguments. sys.argv[0] is the script name itself,
    # so sys.argv[1] is our first actual operational argument.
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    print("Initializing static site generation build pipeline...")
    print(f"Targeting build with basepath routing: '{basepath}'")
    
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
    
    # 3. Compile markdown with structural basepath rules forwarded down
    print(f"Building HTML files recursively from {CONTENT_DIR}...")
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_FILE, DST_DIR, basepath)
    
    print("Full site architecture build pipeline completed successfully!")

if __name__ == "__main__":
    main()
