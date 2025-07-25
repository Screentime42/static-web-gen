from enum import Enum
import re

class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"
   
starts_with_char = lambda markdown, char: all(line.startswith(char) for line in markdown.splitlines())

def is_ordered_list(markdown) -> bool:
   lines = markdown.splitlines()
   for i, line in enumerate(lines, start=1):
      expected_prefix = f"{i}. "
      if not line.startswith(expected_prefix):
         return False
   return True


def block_to_block_type(markdown):
   if re.match(r"^#{1,6}(?!#)\s", markdown):
      return BlockType.HEADING
   
   elif markdown.startswith("```") and markdown.endswith("```"):
      return BlockType.CODE
   
   elif starts_with_char(markdown, ">"):
      return BlockType.QUOTE

   elif starts_with_char(markdown, "- "):
      return BlockType.UNORDERED_LIST
   
   elif is_ordered_list(markdown):
      return BlockType.ORDERED_LIST

   return BlockType.PARAGRAPH
