from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

def text_to_textnodes(text):
   splitters = [
      lambda fragment: split_nodes_delimiter(fragment, "`", TextType.CODE),
      split_nodes_link,
      split_nodes_image,
      lambda fragment: split_nodes_delimiter(fragment, "**", TextType.BOLD),
      lambda fragment: split_nodes_delimiter(fragment, "_", TextType.ITALIC),
   ]

   # If receiving an input node, not a string, use it directly; otherwise, wrap
   if isinstance(text,TextNode):
      to_process = [text]
   else:
      to_process = [TextNode(text, TextType.TEXT)]
   processed = []

   while to_process:
      fragment = to_process.pop(0)

      # Only process plain text nodes for further splitting
      if isinstance(fragment, TextNode) and fragment.text_type != TextType.TEXT:
         processed.append(fragment)
         continue

      # Try each splitter in order, passing a list of [node] 
      for splitter in splitters:
         text_nodes = [fragment] if isinstance(fragment, TextNode) else [TextNode(fragment, TextType.TEXT)]
         result = splitter(text_nodes)
         # If splitting occurred (produced different nodes), process them next
         if len(result) > 1 or result[0] != fragment:
            # Insert new fragments at front to process in order
            to_process = result + to_process
            break
      else:
         # If no splitter acted, mark node as done
         processed.append(fragment)
         
   return processed


