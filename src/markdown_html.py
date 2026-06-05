from parentnode import ParentNode
from leafnode import LeafNode
#from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
#from blocktype import markdown_to_blocks, block_to_block_type, BlockType
from block_markdown import markdown_to_blocks
from blocktype import block_to_block_type, BlockType

from text_to_textnode import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    # 1. Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    
    # 2. Loop over each block and determine its type
    for block in blocks:
        block_type = block_to_block_type(block)
        
        # 3 & 4. Create the proper ParentNode structure based on block type
        if block_type == BlockType.HEADING:
            node = create_heading_node(block)
        elif block_type == BlockType.CODE:
            node = create_code_node(block)
        elif block_type == BlockType.QUOTE:
            node = create_quote_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = create_unordered_list_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = create_ordered_list_node(block)
        else:
            node = create_paragraph_node(block)
            
        block_nodes.append(node)
        
    # 5. Wrap all block nodes inside a ParentNode <div> container
    return ParentNode("div", block_nodes)


# ==========================================
# SHARED INLINE HELPER
# ==========================================

def text_to_children(text):
    """Converts raw inline text into a list of HTML leaf/child nodes."""
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


# ==========================================
# BLOCK-SPECIFIC BUILDER HELPERS
# ==========================================

def create_paragraph_node(block):
    inline_text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(inline_text))


def create_heading_node(block):
    parts = block.split(" ", 1)
    hashes = parts[0]
    heading_text = parts[1]
    level = len(hashes)
    return ParentNode(f"h{level}", text_to_children(heading_text))


def create_code_node(block):
    # Extract raw code text from inside triple backticks
    code_text = block.strip("`").strip("\n")
    
    # Raw code blocks bypass standard inline markdown parsing
    code_leaf = LeafNode(None, code_text)
    
    # Wrap code block structures sequentially
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])


def create_quote_node(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line.lstrip(">").strip())
        
    quote_text = " ".join(cleaned_lines)
    return ParentNode("blockquote", text_to_children(quote_text))


def create_unordered_list_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        item_text = line[2:] # Slice off the "- " marker
        li_nodes.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ul", li_nodes)


def create_ordered_list_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        parts = line.split(". ", 1) # Slice off the dynamic counter sequence e.g., "1. "
        item_text = parts[1]
        li_nodes.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ol", li_nodes)
