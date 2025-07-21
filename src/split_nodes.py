from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

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


def split_nodes_image(old_nodes):
   result = []
   for node in old_nodes:
      if node.text_type == TextType.TEXT:
         current_text = node.text
         images = extract_markdown_images(node.text)    
         if not images:
            result.append(node)
            continue

         for image in images:
            image_alt, image_link = image
            parts = current_text.split(f"![{image_alt}]({image_link})", 1)

            if parts[0]:
               result.append(TextNode(parts[0], TextType.TEXT))

            result.append(TextNode(image_alt, TextType.IMAGE, image_link))

            current_text = parts[1]

         if current_text:
            result.append(TextNode(current_text, TextType.TEXT))

      else:
         result.append(node)
   return result


def split_nodes_link(old_nodes):
   result = []
   for node in old_nodes:
      if node.text_type == TextType.TEXT:
         current_text = node.text
         links = extract_markdown_links(node.text)
         if not links:
            result.append(node)
            continue

         for link in links:
            link_text, link_url = link
            parts = current_text.split(f"[{link_text}]({link_url})", 1)

            if parts[0]:
               result.append(TextNode(parts[0], TextType.TEXT))

            result.append(TextNode(link_text, TextType.LINK, link_url))

            current_text = parts[1]

         if current_text:
            result.append(TextNode(current_text, TextType.TEXT))

      else:
         result.append(node)
   return result