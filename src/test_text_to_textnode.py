import unittest
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    
    def test_everything_combined(self):
        # Testing your exact example block containing all supported syntax types
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected, nodes)

    def test_plain_text_only(self):
        text = "This has absolutely no markdown styling inside it."
        nodes = text_to_textnodes(text)
        expected = [TextNode("This has absolutely no markdown styling inside it.", TextType.TEXT)]
        self.assertListEqual(expected, nodes)

    def test_multiple_of_same_type(self):
        text = "This is **bold** text and this is **also bold** text."
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text and this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_unclosed_delimiter_exception(self):
        # Ensures that the nested split_nodes_delimiter still screams
        # if a user leaves a style tag hanging open
        text = "This has an unclosed **bold element here."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_adjacent_elements(self):
        # Verifies that processing right up against the boundaries works smoothly
        text = "**bold**_italic_`code`[link](url)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertListEqual(expected, nodes)

if __name__ == "__main__":
    unittest.main()
