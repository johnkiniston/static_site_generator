from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)
        
        # If no images are found, keep the text node as-is
        if len(images) == 0:
            new_nodes.append(node)
            continue

        # Process the first image found
        image_alt, image_url = images[0]
        markdown_syntax = f"![{image_alt}]({image_url})"
        
        # Split the text into two parts: before the image and after the image
        sections = original_text.split(markdown_syntax, 1)
        
        # If there is text before the image, add it as a TEXT node
        if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
        # Add the IMAGE node itself
        new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
        
        # If there is remaining text, recursively process it to catch any subsequent images
        if sections[1] != "":
            remaining_nodes = split_nodes_image([TextNode(sections[1], TextType.TEXT)])
            new_nodes.extend(remaining_nodes)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)
        
        # If no links are found, keep the text node as-is
        if len(links) == 0:
            new_nodes.append(node)
            continue

        # Process the first link found
        link_text, link_url = links[0]
        markdown_syntax = f"[{link_text}]({link_url})"
        
        # Split the text into two parts: before the link and after the link
        sections = original_text.split(markdown_syntax, 1)
        
        # If there is text before the link, add it as a TEXT node
        if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
        # Add the LINK node itself
        new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        
        # If there is remaining text, recursively process it to catch any subsequent links
        if sections[1] != "":
            remaining_nodes = split_nodes_link([TextNode(sections[1], TextType.TEXT)])
            new_nodes.extend(remaining_nodes)

    return new_nodes
