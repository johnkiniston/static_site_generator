import re

def extract_markdown_images(text):
    # Pattern explanation:
    # !       -> Matches the literal '!' for images
    # \[(.*?)\] -> Matches the opening and closing square brackets, capturing the alt text inside
    # \((.*?)\) -> Matches the opening and closing parentheses, capturing the URL inside
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    # Pattern explanation:
    # (?<!!)   -> Negative Lookbehind: ensure there is NO '!' right before the brackets
    #             This keeps us from accidentally matching images as links.
    # \[(.*?)\] -> Matches the anchor text
    # \((.*?)\) -> Matches the URL
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)
