import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
   def test_split_nodes_bold(self):
      node = TextNode("This word should be **bold**. Yep.", TextType.TEXT)
      result = split_nodes_delimiter([node], "**", TextType.BOLD)

      expected = [
         TextNode("This word should be ", TextType.TEXT),
         TextNode("bold", TextType.BOLD),
         TextNode(". Yep.", TextType.TEXT),
      ]
      self.assertEqual(result, expected)


   def test_split_nodes_italic(self):
      node = TextNode("This is *italic*, I swear.", TextType.TEXT)
      result = split_nodes_delimiter([node], "*", TextType.ITALIC)

      expected = [
         TextNode("This is ", TextType.TEXT),
         TextNode("italic", TextType.ITALIC),
         TextNode(", I swear.", TextType.TEXT),
      ]
      self.assertEqual(result, expected)

   
   def test_split_nodes_code(self):
      node = TextNode("Check out this piece of `code`, did you look?", TextType.TEXT)
      result = split_nodes_delimiter([node], "`", TextType.CODE)

      expected = [
         TextNode("Check out this piece of ", TextType.TEXT),
         TextNode("code", TextType.CODE),
         TextNode(", did you look?", TextType.TEXT),
      ]
      self.assertEqual(result, expected)


   def test_split_nodes_multiple(self):
      node = TextNode("This is **bold** and this is also **bold**.", TextType.TEXT)
      result = split_nodes_delimiter([node], "**", TextType.BOLD)

      expected = [
         TextNode("This is ", TextType.TEXT),
         TextNode("bold", TextType.BOLD),
         TextNode(" and this is also ", TextType.TEXT),
         TextNode("bold", TextType.BOLD),
         TextNode(".", TextType.TEXT),
      ]
      self.assertEqual(result, expected)

   
   def test_split_nodes_none(self):
      node = TextNode("This is just a normal sentence.", TextType.TEXT)
      result = split_nodes_delimiter([node], "**", TextType.BOLD)

      expected = [
         TextNode("This is just a normal sentence.", TextType.TEXT),
      ]
      self.assertEqual(result, expected)

# TEST SPLIT_NODES_IMAGE

   def test_single_image_split(self):
      node = TextNode(
         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another",
         TextType.TEXT
      )
      result = split_nodes_image([node])

      expected = [
         TextNode("This is text with an ", TextType.TEXT),
         TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
         TextNode(" and another", TextType.TEXT)
      ]

      self.assertEqual(result, expected)
   

   def test_no_images_to_split(self):
      node = TextNode("This is just a normal sentence. No images.", TextType.TEXT)

      result = split_nodes_image([node])

      expected = [
         TextNode("This is just a normal sentence. No images.", TextType.TEXT),
         ]
      self.assertEqual(result, expected)


   def test_multiple_image_split(self):
      node = TextNode(
         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another one ![image](https://i.imgur.com/zjjcJKZ.png)",
         TextType.TEXT
      )
      result = split_nodes_image([node])

      expected = [
         TextNode("This is text with an ", TextType.TEXT),
         TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
         TextNode(" and another one ", TextType.TEXT),
         TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
      ]

      self.assertEqual(result, expected)


# TEST SPLIT_NODES_LINK

   def test_split_node_link(self):
      node = TextNode("This is text with a link to [Google](https://www.google.com)", TextType.TEXT)
      result = split_nodes_link([node])

      expected = [
         TextNode("This is text with a link to ", TextType.TEXT),
         TextNode("Google", TextType.LINK, "https://www.google.com")
      ]

      self.assertEqual(result, expected)

   
   def test_split_node_no_link(self):
      node = TextNode("This is just text with no link.", TextType.TEXT)
      result = split_nodes_link([node])

      expected = [
         TextNode("This is just text with no link.", TextType.TEXT),
      ]

      self.assertEqual(result, expected)


   def test_split_node_multiple_links(self):
      node = TextNode("This is text with a link to [Google](https://www.google.com) and you should check your [Twitter](https://www.Twitter.com)", TextType.TEXT)
      result = split_nodes_link([node])

      expected = [
         TextNode("This is text with a link to ", TextType.TEXT),
         TextNode("Google", TextType.LINK, "https://www.google.com"),
         TextNode(" and you should check your ", TextType.TEXT),
         TextNode("Twitter", TextType.LINK, "https://www.Twitter.com"),
      ]

      self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()