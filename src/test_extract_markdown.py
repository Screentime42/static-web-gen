import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
   def test_extract_markdown_images(self):
      matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
      )
      self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

   
   def test_extract_markdown_links(self):
      matches = extract_markdown_links(
         "This is text with a link [to Twitter](https://www.twitter.com)"
      )
      self.assertListEqual([("to Twitter", "https://www.twitter.com")], matches)


if __name__ == "__main__":
    unittest.main()