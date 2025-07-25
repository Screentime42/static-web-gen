from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from htmlnode import HTMLNode
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from blocktype import BlockType


def block_type_to_tag(blocktype, block=None):
   if blocktype == BlockType.PARAGRAPH:
      return "p"
   elif blocktype == BlockType.HEADING:
      count, content = heading_handler(block)
      return f"h{count}"
   elif blocktype == BlockType.CODE:
      return "pre"
   elif blocktype == BlockType.UNORDERED_LIST:
      return "ul"
   elif blocktype == BlockType.ORDERED_LIST:
      return "ol"
   else:
      raise Exception("Error: Invalid blocktype")


def heading_handler(block):
   count = len(block) - len(block.lstrip("#"))
   content = block.lstrip("#").lstrip()
   return count, content


def text_to_children(blocktype, block):
   if blocktype == BlockType.CODE:
      lines = block.split('\n')
      code_value = '\n'.join(lines[1:-1]) + '\n'
      code_node = HTMLNode(tag="code", value=code_value)
      return HTMLNode(tag="pre", children=[code_node])

      
   elif blocktype == BlockType.HEADING:
      _, heading_content = heading_handler(block)
      tag = block_type_to_tag(blocktype, block)
      textnodes = text_to_textnodes(heading_content)
      children = [text_node_to_html_node(node) for node in textnodes]
      return HTMLNode(tag=tag, children=children)
   
   elif blocktype == BlockType.PARAGRAPH:
      tag = block_type_to_tag(blocktype, block)
      paragraph_content = " ".join(block.splitlines())
      textnodes = text_to_textnodes(paragraph_content)
      children = [text_node_to_html_node(node) for node in textnodes]
      return HTMLNode(tag=tag, children=children)
   
   else:
      tag = block_type_to_tag(blocktype, block)
      textnodes = text_to_textnodes(block)
      children = [text_node_to_html_node(node) for node in textnodes]
      return HTMLNode(tag=tag, children=children)
   

def markdown_to_html_node(markdown):
   blocks = markdown_to_blocks(markdown)
   html_blocks = []
   for block in blocks:
      blocktype = block_to_block_type(block)
      node = text_to_children(blocktype, block)
      html_blocks.append(node)
   
   parent_node = HTMLNode(tag="div", children=html_blocks)
   return parent_node




