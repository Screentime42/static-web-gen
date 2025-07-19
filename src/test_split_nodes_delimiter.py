import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
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


   


if __name__ == "__main__":
    unittest.main()