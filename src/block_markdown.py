def markdown_to_blocks(markdown):
    # Split the raw document by double newlines
    raw_blocks = markdown.split("\n\n")
    filtered_blocks = []
    
    for block in raw_blocks:
        # Strip leading/trailing whitespaces (spaces, tabs, single newlines)
        cleaned_block = block.strip()
        
        # Only add the block if it contains actual text content
        if cleaned_block != "":
            filtered_blocks.append(cleaned_block)
            
    return filtered_blocks
