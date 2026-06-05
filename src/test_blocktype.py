import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):

    def test_headings_and_paragraphs(self):
        # Valid H1 and H6 headers
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        
        # Invalid headers (should fall back to PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#NoSpaceAfterHash"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Plain old paragraph text."), BlockType.PARAGRAPH)

    def test_code_blocks(self):
        # Fixed: Clean multiline code block wrapped in triple quotes
        code_block = """```
def hello():
    print('world')
```"""
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        
        # Missing closing backticks
        invalid_code = "```\nmissing closing backticks"
        self.assertEqual(block_to_block_type(invalid_code), BlockType.PARAGRAPH)

    def test_quote_blocks(self):
        # Fixed: Every line starts with > wrapped in triple quotes
        quote_block = """> This is a quote
> that spans across
> multiple lines."""
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        
        # One line is missing the > indicator
        invalid_quote = """> Line one
Line two missing character
> Line three"""
        self.assertEqual(block_to_block_type(invalid_quote), BlockType.PARAGRAPH)

    def test_unordered_lists(self):
        # Fixed: Clean unordered list block wrapped in triple quotes
        ul_block = """- Item one
- Item two
- Item three"""
        self.assertEqual(block_to_block_type(ul_block), BlockType.UNORDERED_LIST)
        
        # Missing space after the dash on the second item
        invalid_ul = """- Item one
-Item two missing space
- Item three"""
        self.assertEqual(block_to_block_type(invalid_ul), BlockType.PARAGRAPH)

    def test_ordered_lists(self):
        # Fixed: Clean, perfectly incrementing ordered list block wrapped in triple quotes
        ol_block = """1. First
2. Second
3. Third"""
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)
        
        # Broken numbering increment sequence (skips to 3)
        invalid_ol_sequence = """1. First
3. Broken order
4. Third"""
        self.assertEqual(block_to_block_type(invalid_ol_sequence), BlockType.PARAGRAPH)
        
        # Doesn't start at number 1
        invalid_ol_start = """2. Item one
3. Item two"""
        self.assertEqual(block_to_block_type(invalid_ol_start), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
