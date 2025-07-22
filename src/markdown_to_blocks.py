import textwrap

def markdown_to_blocks(markdown):
   markdown = textwrap.dedent(markdown)
   strings = markdown.split("\n\n")
   cleaned_blocks = []
   for string in strings:
      stripped = string.strip()
      if stripped: 
         cleaned_blocks.append(stripped)

   return cleaned_blocks                     