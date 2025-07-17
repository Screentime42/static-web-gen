from enum import Enum

class TextType(Enum):
   PLAIN = "plain"       # e.g. text
   BOLD = "bold"         # e.g. **text**
   ITALIC = "italic"       # e.g. _text_
   CODE = "code"         # e.g. `text`
   LINK = "link"         # e.g. [anchor text](url)
   IMAGE = "image"        # e.g. ![alt](url)

class TextNode:
   def __init__(self, text, text_type, url=None):
      self.text = text
      self.text_type = text_type
      self.url = url

   def __eq__(self, other):
      if not isinstance(other, TextNode):
         return False
      return (
         self.text == other.text and
         self.text_type == other.text_type and
         self.url == other.url
      )
   
   def __repr__(self):
      return f"TextNode({self.text!r}, {self.text_type}, {self.url!r})"