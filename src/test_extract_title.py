import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_standard_title(self):
        # 1. Basic clean title extraction
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_title_with_extra_whitespace(self):
        # 2. Leading/trailing whitespace inside and around the header is stripped
        markdown = "   #    My Awesome Title   "
        self.assertEqual(extract_title(markdown), "My Awesome Title")

    def test_title_mid_document(self):
        # 3. Title found deep inside a multiline document
        markdown = """This is an introductory paragraph.

# Document Title

Some more trailing text here."""
        self.assertEqual(extract_title(markdown), "Document Title")

    def test_no_h1_exception(self):
        # 4. Correctly raises ValueError when no H1 is present
        markdown = """## Subheading Only
This document has no main title."""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_ignores_other_headers(self):
        # 5. Ensures it skips H2/H3 tags and specifically grabs the H1
        markdown = """## Section 1
### Subsection
# Actual Title
## Section 2"""
        self.assertEqual(extract_title(markdown), "Actual Title")

if __name__ == "__main__":
    unittest.main()
