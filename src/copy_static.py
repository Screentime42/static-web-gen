import os
import shutil

def copy_static():
   source = "static"
   destination = "docs"
   
   if os.path.exists(destination):
      shutil.rmtree(destination)
   os.mkdir(destination)

   def recursive_copy(src, dst):
      for item in os.listdir(src):
         src_item = os.path.join(src, item)
         dst_item = os.path.join(dst, item)

         if os.path.isfile(src_item):
            shutil.copy(src_item, dst_item)
            print(f"Copied file: {dst_item}")
         else:
            os.mkdir(dst_item)
            print(f"Created directory: {dst_item}")
            recursive_copy(src_item, dst_item)
   
   recursive_copy(source, destination)