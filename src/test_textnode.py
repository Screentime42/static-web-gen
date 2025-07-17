import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
   def test_eq(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.BOLD)
      self.assertEqual(node, node2)

   def test_not_eq(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.ITALIC)
      self.assertNotEqual(node, node2)

   def test_not_eq_text(self):
      node = TextNode("This is a text node", TextType.PLAIN)
      node2 = TextNode("This is still a text node just different", TextType.PLAIN)
      self.assertNotEqual(node, node2)

   def test_not_eq_diff_url(self):
      node = TextNode("Link1", TextType.LINK, "www.boot.dev")
      node2 = TextNode("Link1", TextType.LINK, "www.bootdev.com")
      self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()