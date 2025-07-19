from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
   result = []
   for node in old_nodes:
      if node.text_type != TextType.TEXT:
         result.append(node)
      else:
         parts = node.text.split(delimiter)
         if len(parts) % 2 == 0:
            raise Exception("Invalid markdown: missing closing delimiter")
         for i, part in enumerate(parts):
            if not part:
               continue
            if i % 2 == 0:
               result.append(TextNode(part, TextType.TEXT))
            else:
               result.append(TextNode(part, text_type))
   return result