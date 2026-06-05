from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    # 1. Heading Validation
    # Checks if it starts with 1-6 '#' followed by a space
    if block.startswith("#") and " " in block:
        # Separate the potential hash sequence from the text
        parts = block.split(" ", 1)
        hashes = parts[0]
        if len(hashes) <= 6 and all(c == "#" for c in hashes):
            return BlockType.HEADING

    # 2. Code Block Validation
    # Must start with 3 backticks and end with 3 backticks
    if block.startswith("```") and block.endswith("```") and len(block) >= 6:
        return BlockType.CODE

    # Split into individual lines to validate multiline blocks (quotes and lists)
    lines = block.split("\n")

    # 3. Quote Block Validation
    # Every line must start with '>'
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # 4. Unordered List Validation
    # Every line must start with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # 5. Ordered List Validation
    # Every line must start with a strictly incrementing counter starting at 1: "1. ", "2. ", etc.
    is_ordered_list = True
    for i in range(len(lines)):
        expected_start = f"{i + 1}. "
        if not lines[i].startswith(expected_start):
            is_ordered_list = False
            break
            
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    # 6. Fallback
    return BlockType.PARAGRAPH
