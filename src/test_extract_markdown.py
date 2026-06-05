import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links 
# Note: Adjust the 'from' import statement above to match whatever file 
# your extraction functions are saved in!

class TestMarkdownExtraction(unittest.TestCase): # Class starts at the far left

    def test_extract_markdown_images(self): # Indented 4 spaces
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self): # Indented 4 spaces
        text = "![one](url1.png) text ![two](url2.jpg) text ![three](url3.gif)"
        matches = extract_markdown_images(text)
        expected = [
            ("one", "url1.png"),
            ("two", "url2.jpg"),
            ("three", "url3.gif")
        ]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_links(self): # Indented 4 spaces
        text = "Click [here](https://www.boot.dev) to learn coding!"
        matches = extract_markdown_links(text)
        self.assertListEqual([("here", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self): # Indented 4 spaces
        text = "Go [home](/) or visit [google](https://google.com)"
        matches = extract_markdown_links(text)
        expected = [
            ("home", "/"),
            ("google", "https://google.com")
        ]
        self.assertListEqual(expected, matches)

    def test_links_do_not_match_images(self): # Indented 4 spaces
        text = "This is a link [anchor](link_url) and this is an image ![alt](img_url)"
        link_matches = extract_markdown_links(text)
        image_matches = extract_markdown_images(text)
        
        self.assertListEqual([("anchor", "link_url")], link_matches)
        self.assertListEqual([("alt", "img_url")], image_matches)

if __name__ == "__main__":
    unittest.main()
