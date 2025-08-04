import unittest

from main import extract_title

class TestMain(unittest.TestCase):
   def test_heading_extract_present(self):
      node = """
      # Heading 1

      This is some random text
      and a list:
      - abc
      - def
      """
      result = extract_title(node)
      self.assertEqual(result, "Heading 1")

   
   def test_heading_extract_not_present(self):
      node = """
      

      This is some random text
      and a list:
      - abc
      - def
      """
      with self.assertRaises(Exception):
         extract_title(node)
      


   def test_heading_extract_whitespace(self):
      node = """
             # Heading 1    

      This is some random text
      and a list:
      - abc
      - def
      """
      result = extract_title(node)
      self.assertEqual(result, "Heading 1")
   

   def test_heading_extract_other_heading(self):
      node = """
      ### Heading 3

      This is some random text
      and a list:
      - abc
      - def
      """
      with self.assertRaises(Exception):
         extract_title(node)



if __name__ == "__main__":
    unittest.main()