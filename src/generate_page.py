import os
from markdown_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # 1. Read the raw markdown content
    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Source markdown file not found at: {from_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
        
    # 2. Read the HTML template content
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template HTML file not found at: {template_path}")
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    # 3. Convert markdown block node tree to flat HTML string
    html_node = markdown_to_html_node(markdown_content)
    content_html = html_node.to_html()
    
    # 4. Extract the main document page title
    page_title = extract_title(markdown_content)
    
    # 5. Inject the values into our template placeholders
    full_html = template_content.replace("{{ Title }}", page_title)
    full_html = full_html.replace("{{ Content }}", content_html)
    
    # 6. Ensure the destination directory path exists before writing
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        print(f"Creating missing directory tree structure: {dest_dir}")
        os.makedirs(dest_dir)
        
    # 7. Write out the final, fully-rendered HTML artifact
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully generated page: {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Crawls the content directory recursively and generates HTML files 
    for every markdown file found, mirroring the exact directory structure.
    """
    # 1. List all items inside the current content directory level
    items = os.listdir(dir_path_content)
    
    for item in items:
        # Create full paths for the source item and its projected public destination
        src_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(src_path):
            # 2. Check if the file is a markdown file
            if item.endswith(".md"):
                # Swap out the .md extension for .html for the output file
                html_filename = item[:-3] + ".html"
                dst_path = os.path.join(dest_dir_path, html_filename)
                
                # Use our existing single page generation tool to build the artifact
                generate_page(src_path, template_path, dst_path)
                
        else:
            # 3. Recursive step: If it's a directory, dive into it 
            # and project its path structure forward into the destination folder
            new_dest_path = os.path.join(dest_dir_path, item)
            print(f"Directory found. Descending into: {src_path} -> {new_dest_path}")
            generate_pages_recursive(src_path, template_path, new_dest_path)
