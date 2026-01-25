from textnode import *
from htmlnode import *

def main(): 
    print("Hello There")
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node.to_html())
    
    
    
if __name__ == "__main__":
    main()