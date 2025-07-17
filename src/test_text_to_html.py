import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode
from text_to_html import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
   def test_text(self):
      node = TextNode("This is normal text", TextType.TEXT)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is normal text")

   
   def test_bold(self):
      node = TextNode("This is bold", TextType.BOLD)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "b")
      self.assertEqual(html_node.value, "This is bold")


   def test_italic(self):
      node = TextNode("This is italic", TextType.ITALIC)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "i")
      self.assertEqual(html_node.value, "This is italic")

   
   def test_code(self):
      node = TextNode("This is a code snippet", TextType.CODE)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "code")
      self.assertEqual(html_node.value, "This is a code snippet")

   
   def test_link(self):
      node = TextNode("Click me", TextType.LINK, "https://boot.dev")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "a")
      self.assertEqual(html_node.value, "Click me")
      self.assertEqual(html_node.props["href"], "https://boot.dev")

   
   def test_image(self):
      node = TextNode("Programming image", TextType.IMAGE, "https://boot.dev/image")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "img")
      self.assertEqual(html_node.value, "")
      self.assertEqual(html_node.props["src"], "https://boot.dev/image")
      self.assertEqual(html_node.props["alt"], "Programming image")


if __name__ == "__main__":
    unittest.main()


