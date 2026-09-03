import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith('# '):
          return line.strip('#').strip()
        else:
           raise ValueError("no title found")

def generate_page(from_path: str, template_path: str, dest_path: str | Path) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path, "r")
    markdown_content = md_file.read()
    md_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', content)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for entry in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        print(entry)
        if os.path.isfile(path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(path, template_path, dest_path)



    