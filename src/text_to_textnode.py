from textnode import TextNode, TextType
from split_image import (
    split_nodes_link,
)
from split_nodes import split_nodes_delimiter
from split_image import split_nodes_image

def text_to_textnodes(text):
    # Start with a single TextNode containing the raw text string
    nodes = [TextNode(text, TextType.TEXT)]
    
    # 1. Split out bold sections (**bold**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # 2. Split out italic sections (_italic_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # 3. Split out inline code sections (`code`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # 4. Split out images (![alt](src))
    nodes = split_nodes_image(nodes)
    
    # 5. Split out links ([anchor](href))
    nodes = split_nodes_link(nodes)
    
    return nodes
