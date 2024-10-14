from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode


def main():
    text_node = TextNode("text node", "bold", "https://123.com")
    print(text_node.text_node_to_html_node())
    # html_node = HTMLNode()
    # html_node.props_to_html()
    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )

    # print(node.to_html())

main()