import os
from markdown_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the raw files
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    # Convert and extract content metadata
    html_node = markdown_to_html_node(markdown_content)
    content_html = html_node.to_html()
    page_title = extract_title(markdown_content)
    
    # Structural template replacement
    full_html = template_content.replace("{{ Title }}", page_title)
    full_html = full_html.replace("{{ Content }}", content_html)
    
    # Production Basepath Replacement Rules:
    # Converts absolute root paths to nested directory rules safely
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    
    # Write output to directory tree location
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """
    Crawls content directory tree, forwarding down basepath properties to the generator.
    """
    items = os.listdir(dir_path_content)
    
    for item in items:
        src_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(src_path):
            if item.endswith(".md"):
                html_filename = item[:-3] + ".html"
                dst_path = os.path.join(dest_dir_path, html_filename)
                
                # Forward basepath down directly to the rendering file script
                generate_page(src_path, template_path, dst_path, basepath)
                
        else:
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(src_path, template_path, new_dest_path, basepath)
