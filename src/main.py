from copy_static import copy_static
from markdown_to_html_node import markdown_to_html_node
import os, shutil




def main():
   if os.path.exists("public"):
      shutil.rmtree("public")
   copy_static()
   generate_pages_recursive("content", "template.html", "public")

def extract_title(markdown):
   lines = markdown.split('\n')
   for line in lines:
      line = line.strip()
      if line.startswith('# '):
         heading = line
         heading_trimmed = heading[1:].strip()
         return heading_trimmed    
   raise Exception('Error: No heading found')


def generate_page(from_path, template_path, dest_path):
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   markdown = open(from_path).read()
   template = open(template_path).read()

   markdown_as_html = markdown_to_html_node(markdown).to_html()
   title = extract_title(markdown)

   template_with_title = template.replace("{{ Title }}", title)
   template_with_content = template_with_title.replace("{{ Content }}", markdown_as_html)

   dest_dir_path = os.path.dirname(dest_path)
   os.makedirs(dest_dir_path, exist_ok=True)

   with open(dest_path, "w") as file:
      file.write(template_with_content)
      print(f"File successfully writted to {dest_path}")
   

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   for dirpath, _, filenames  in os.walk(dir_path_content):
      for filename in filenames:
         if filename.endswith('.md'):
            from_path = os.path.join(dirpath, filename)
            subfolder = os.path.relpath(dirpath, dir_path_content)
            dest_subdir = os.path.join(dest_dir_path, subfolder)
            new_filename = filename[:-3] + ".html"
            out_path = os.path.join(dest_subdir, new_filename)
            generate_page(from_path, template_path, out_path)
   
   


if __name__ == "__main__":
   main()