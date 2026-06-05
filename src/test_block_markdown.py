import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks_standard(self):
        # 1. Tests standard, clean parsing of three basic blocks
        text = """# This is a heading

This is a paragraph of text. It has some **bold** words.

- This is a list item
- This is another list item"""
        
        blocks = markdown_to_blocks(text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** words.",
            "- This is a list item\n- This is another list item"
        ]
        self.assertListEqual(expected, blocks)

    def test_markdown_to_blocks_excessive_newlines(self):
        # 2. Tests that multiple extra empty lines between blocks are ignored
        text = """# Heading




Paragraph text here.


- List item"""
        
        blocks = markdown_to_blocks(text)
        expected = [
            "# Heading",
            "Paragraph text here.",
            "- List item"
        ]
        self.assertListEqual(expected, blocks)

    def test_markdown_to_blocks_whitespace_stripping(self):
        # 3. Tests that leading/trailing spaces and tabs inside blocks are trimmed
        text = """   # Heading with leading spaces   

Paragraph with trailing spaces       

\t   - List item with tabs and spaces   """
        
        blocks = markdown_to_blocks(text)
        expected = [
            "# Heading with leading spaces",
            "Paragraph with trailing spaces",
            "- List item with tabs and spaces"
        ]
        self.assertListEqual(expected, blocks)

    def test_markdown_to_blocks_empty_input(self):
        # 4. Tests that entirely empty strings or strings with just newlines return an empty list
        text = "\n\n\n   \n\n"
        blocks = markdown_to_blocks(text)
        self.assertListEqual([], blocks)

    def test_markdown_to_blocks_single_block(self):
        # 5. Tests that a single block without any double newlines is handled correctly
        text = "Just a single paragraph block with no extra spacing around it."
        blocks = markdown_to_blocks(text)
        self.assertListEqual([text], blocks)

if __name__ == "__main__":
    unittest.main()
