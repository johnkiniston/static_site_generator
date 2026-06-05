import unittest
from textnode import TextNode, TextType
from split_image import split_nodes_link, split_nodes_image

class TestSplitNodesLinkImage(unittest.TestCase):
    
    # ==========================================
    # LINK SPLITTING TESTS
    # ==========================================

    def test_split_single_link(self):
        node = TextNode("Read [bootdev](https://boot.dev) now.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Read ", TextType.TEXT),
            TextNode("bootdev", TextType.LINK, "https://boot.dev"),
            TextNode(" now.", TextType.TEXT),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_multiple_links(self):
        node = TextNode(
            "Link [one](url1) and link [two](url2)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Link ", TextType.TEXT),
            TextNode("one", TextType.LINK, "url1"),
            TextNode(" and link ", TextType.TEXT),
            TextNode("two", TextType.LINK, "url2"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_link_at_start(self):
        node = TextNode("[Start](url) trailing text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Start", TextType.LINK, "url"),
            TextNode(" trailing text", TextType.TEXT),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_link_at_end(self):
        node = TextNode("Leading text [End](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Leading text ", TextType.TEXT),
            TextNode("End", TextType.LINK, "url"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_consecutive_links(self):
        node = TextNode("[one](url1)[two](url2)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("one", TextType.LINK, "url1"),
            TextNode("two", TextType.LINK, "url2"),
        ]
        self.assertListEqual(expected, new_nodes)

    # ==========================================
    # IMAGE SPLITTING TESTS
    # ==========================================

    def test_split_single_image(self):
        node = TextNode("Look at ![cat](cat.jpg) here.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Look at ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.jpg"),
            TextNode(" here.", TextType.TEXT),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_multiple_images(self):
        node = TextNode(
            "![one](img1.png) middle ![two](img2.png)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("one", TextType.IMAGE, "img1.png"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "img2.png"),
        ]
        self.assertListEqual(expected, new_nodes)

    # ==========================================
    # MIXED & PASS-THROUGH TESTS
    # ==========================================

    def test_split_no_matches(self):
        node = TextNode("Just plain text with no links or images.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_ignores_images(self):
        node = TextNode("This is a link [anchor](url) and an image ![alt](img)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        # The image string should remain as unparsed TEXT inside the remaining text node
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("anchor", TextType.LINK, "url"),
            TextNode(" and an image ![alt](img)", TextType.TEXT),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_pass_through_non_text(self):
        # Nodes that aren't TextType.TEXT must be left entirely alone
        nodes = [
            TextNode("already parsed", TextType.LINK, "url"),
            TextNode("raw [link](url)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("already parsed", TextType.LINK, "url"),
            TextNode("raw ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url")
        ]
        self.assertListEqual(expected, new_nodes)

if __name__ == "__main__":
    unittest.main()
