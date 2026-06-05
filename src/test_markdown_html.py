import unittest
from htmlnode import HTMLNode
from markdown_html import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_single_paragraph(self):
        m = "This is a simple paragraph string."
        node = markdown_to_html_node(m)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children[0].tag, "p")

    def test_paragraph_with_inline(self):
        m = "Paragraph with **bold** and _italic_ elements."
        node = markdown_to_html_node(m)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].children[1].tag, "b")

    def test_heading_h1(self):
        node = markdown_to_html_node("# Title")
        self.assertEqual(node.children[0].tag, "h1")

    def test_code_block(self):
        node = markdown_to_html_node("```\nprint(1)\n```")
        self.assertEqual(node.children[0].tag, "pre")
        self.assertEqual(node.children[0].children[0].tag, "code")

    def test_blockquote(self):
        node = markdown_to_html_node("> Quote")
        self.assertEqual(node.children[0].tag, "blockquote")

    def test_unordered_list(self):
        node = markdown_to_html_node("- A\n- B")
        self.assertEqual(node.children[0].tag, "ul")

    def test_ordered_list(self):
        node = markdown_to_html_node("1. A\n2. B")
        self.assertEqual(node.children[0].tag, "ol")

if __name__ == "__main__":
    unittest.main()
