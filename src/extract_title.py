def extract_title(markdown):
    # Split the document into individual lines
    lines = markdown.split("\n")
    
    for line in lines:
        # Strip any leading spaces before checking for the header symbol
        cleaned_line = line.strip()
        
        # Check if the line starts with a single '#' followed by a space
        if cleaned_line.startswith("# "):
            # Slice off the '# ' prefix and strip any extra whitespace from the text
            return cleaned_line[2:].strip()
            
    # If the loop finishes without finding an H1 header, scream
    raise ValueError("No H1 header found in the markdown document.")
