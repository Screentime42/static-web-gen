import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


print("Test file is running!")


class TestHTMLNode(unittest.TestCase):
   def test_props_to_html_with_multiple_props(self):
      # Test description: props_to_html should format multiple attribs correctly
      node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})

      result = node.props_to_html()

      expected = ' href="https://example.com" target="_blank"'
      self.assertEqual(result, expected)

   def test_props_to_html_empty_props(self):
      # Test description: props_to_html should handle empty props
      node = HTMLNode()

      result = node.props_to_html()

      self.assertEqual(result, "")

   def test_constructor_with_app_parameters(self):
      # Test description: __init__ should create a HTMLNode with all parameters
      node = HTMLNode(
         tag="p",
         value="Hello world",
         children=[],
         props={"class": "text"}
      )

      self.assertEqual(node.tag, "p")
      self.assertEqual(node.value, "Hello world")
      self.assertEqual(node.children, [])
      self.assertEqual(node.props, {"class": "text"})

   def test_constructor_defaults_to_none(self):
      # Test description: __init__ should create HTMLNode and parameters should default to none if left emtpy
      node = HTMLNode()

      self.assertIsNone(node.tag)
      self.assertIsNone(node.value)
      self.assertIsNone(node.children)
      self.assertIsNone(node.props)

   def test_repr_shows_node_info(self):
      # Test description: __repr__ should print node info
      node = HTMLNode(tag="a", value="Click me", props={"href": "test.com"})

      result = repr(node)

      self.assertIn("a", result)
      self.assertIn("Click me", result)
      self.assertIn("href", result)


   # LEAFNODE TESTS

   def test_leaf_to_html_p(self):
      node = LeafNode("p", "Hello, world!")
      self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
   
   def test_leaf_to_html_a(self):
      node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
      self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click me!</a>')

   def test_leaf_to_html_h1(self):
      node = LeafNode("h1", "This is a header")
      self.assertEqual(node.to_html(), "<h1>This is a header</h1>")

   def test_leaf_to_html_no_value(self):
      node = LeafNode("p", None)
      self.assertRaises(ValueError, node.to_html)

   def test_leaf_to_html_tag_is_none(self):
      node = LeafNode(None, "Raw text?")
      self.assertEqual(node.to_html(), "Raw text?")


   # PARENTNODE TESTS

   def test_simple_rendering(self):
      node = ParentNode("p", [LeafNode(None, "Hello world!")])
      self.assertEqual(node.to_html(), "<p>Hello world!</p>")

   def test_rendering_with_tagged_children(self):
      node = ParentNode("p", [
         LeafNode("b", "Bold"),
         LeafNode(None, " and plain."),
         LeafNode("i", " Italic")
      ])
      expected = "<p><b>Bold</b> and plain.<i> Italic</i></p>"
      self.assertEqual(node.to_html(), expected)

   def test_props_rendering(self):
      node = ParentNode("p", [LeafNode(None, "Hi")], props={"class": "intro"})
      self.assertEqual(node.to_html(), '<p class="intro">Hi</p>')
      
   def test_missing_tag_raises(self):
      with self.assertRaises(ValueError):
         ParentNode(None, [LeafNode(None, "Hi")])

   def test_missing_children_raises(self):
      with self.assertRaises(ValueError):
         ParentNode("p", None)
   

if __name__ == "__main__":
    unittest.main()