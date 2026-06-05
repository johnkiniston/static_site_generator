import os
import shutil

def copy_directory_recursive(source, destination):
    """
    Recursively copies all contents from source directory to destination directory.
    """
    # 1. Ensure the destination directory exists
    if not os.path.exists(destination):
        print(f"Creating directory: {destination}")
        os.mkdir(destination)

    # 2. List all items inside the current source directory
    items = os.listdir(source)
    
    for item in items:
        # Create full paths for both source and destination
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)
        
        # 3. Base Case: If it's a file, copy it directly
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
            
        # 4. Recursive Step: If it's a directory, dive into it
        else:
            print(f"Entering directory: {src_path}")
            copy_directory_recursive(src_path, dst_path)
