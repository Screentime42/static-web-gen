

class HTMLNode:
   def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag  # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
      self.value = value  # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
      self.children = children # A list of HTMLNode objects representing the children of this node
      self.props = props  #  A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

   def to_html(self):
      if self.tag is None:
         return self.value or ""
      children_html = "".join(child.to_html() for child in (self.children or []))
      props_str = ""
      if self.props:
         props_pairs = [f'{key}="{value}"' for key, value in self.props.items()]
         props_str = " " + " ".join(props_pairs)
      content = children_html if children_html else (self.value or "")
      return f"<{self.tag}{props_str}>{content}</{self.tag}>"
   
   def props_to_html(self):
      if not self.props:
         return ""
      return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
   
   def __repr__(self):
      return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

   
class LeafNode(HTMLNode):
   def __init__(self, tag, value, props=None):
      super().__init__(tag, value, children=None, props=props)
      
   def to_html(self):
      if not self.value:
         raise ValueError("All leaf nodes must have a value")
      if self.tag == None:
         return self.value
      props_str = self.props_to_html() if self.props else ""
      return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
   

class ParentNode(HTMLNode):
   def __init__(self, tag, children, props=None):
      super().__init__(tag=tag, value=None, children=children, props=props)
      if not self.tag:
         raise ValueError("ParentNode must have a tag")
      if not self.children:
         raise ValueError("ParentNode must have children defined")
      
   def to_html(self):
      if self.tag == None:
         raise ValueError("ParentNode must have a tag")
      if self.children == None:
         raise ValueError("ParentNode must have children defined")
      
      props_str = self.props_to_html() if self.props else ""
      inner_html = "".join(child.to_html() for child in self.children)
      return f'<{self.tag}{props_str}>{inner_html}</{self.tag}>'
      