import unittest
import textwrap
from blocktype import *


class TestBlockType(unittest.TestCase):
   def test_paragraph(self):
      node = "This is just a simple paragraph, nothing else."
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_heading(self):
      node = "## HEADING2"
      result = block_to_block_type(node)
      expected = BlockType.HEADING

      self.assertEqual(result, expected)
      

   def test_heading_too_many(self):
      node = "####### HEADING2"
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_heading_no_space(self):
      node = "##HEADING2"
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_code(self):
      node = "```if this == code, return nice```"
      result = block_to_block_type(node)
      expected = BlockType.CODE

      self.assertEqual(result, expected)
   

   def test_code_not_closed(self):
      node = "```if this == code, return nice"
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_quote(self):
      node = "\n".join([
         "> To be,",
         "> or not to be?",
         "> that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.QUOTE

      self.assertEqual(result, expected)


   def test_unordered_list(self):
      node = "\n".join([
         "- To be,",
         "- or not to be?",
         "- that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.UNORDERED_LIST

      self.assertEqual(result, expected)


   def test_unordered_list_no_space(self):
      node = "\n".join([
         "-To be,",
         "-or not to be?",
         "-that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_ordered_list(self):
      node = "\n".join([
         "1. To be,",
         "2. or not to be?",
         "3. that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.ORDERED_LIST

      self.assertEqual(result, expected)


   def test_ordered_list_wrong_num(self):
      node = "\n".join([
         "1. To be,",
         "2. or not to be?",
         "4. that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


   def test_ordered_list_no_period(self):
      node = "\n".join([
         "1. To be,",
         "2. or not to be?",
         "3 that is the question."
      ])
      result = block_to_block_type(node)
      expected = BlockType.PARAGRAPH

      self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
