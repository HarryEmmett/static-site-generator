from htmlnode import HTMLNode
from textnode import TextNode

def main():
    # text_node = TextNode("text node", "bold", "https://123.com")
    # print(text_node)
    html_node = HTMLNode()
    html_node.props_to_html()

main()