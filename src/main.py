from textnode import *
from htmlnode import *
from generate_content import*
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    delete_destination_contents(dir_path_public)
    
    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)
    
    print("Generating page...")
    index_path = os.path.join(dir_path_content, "index.md")
    dest_path = os.path.join(dir_path_public, "index.html")
    #generate_page(index_path, template_path, dest_path)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    
    return

     
def delete_destination_contents(folder: str) -> None:
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

def copy_files(source: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(source):
        file_path_source = os.path.join(source, file)
        file_path_dest = os.path.join(dest, file)

        if os.path.isfile(file_path_source):
            shutil.copy(file_path_source, file_path_dest)
            # print(f"Copied: {file} from {file_path_source} to {file_path_dest}")
        else: 
            os.mkdir(file_path_dest)
            copy_files(file_path_source, file_path_dest)


if __name__ == "__main__":
    main()