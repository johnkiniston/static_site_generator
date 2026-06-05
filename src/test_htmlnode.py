import unittest
from htmlnode import HTMLNode  # <--- Add this line

# Assuming your HTMLNode class is in the same file or imported
class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        """Test if multiple attributes are formatted with leading spaces correctly."""
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        """Test that None or empty props return an empty string."""
        node_none = HTMLNode(tag="p", value="Hello", props=None)
        node_empty = HTMLNode(tag="p", value="Hello", props={})
        
        self.assertEqual(node_none.props_to_html(), "")
        self.assertEqual(node_empty.props_to_html(), "")

    def test_constructor_defaults(self):
        """Ensure all data members are None by default."""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        """Check that the __repr__ method outputs the expected debug string."""
        node = HTMLNode(tag="div", value="content")
        expected_repr = "HTMLNode(div, content, children: None, None)"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
