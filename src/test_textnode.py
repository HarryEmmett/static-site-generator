import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text nodeeee", "bold")
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "not bold")
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", "bold")
        node6 = TextNode("This is a text node", "bold", "a url")
        self.assertNotEqual(node5, node6)

    def test_url(self):
        node = TextNode("test", "bold", "a url")
        node2 = TextNode("test", "bold")

        self.assertEqual(node.url, "a url")
        self.assertEqual(node2.url, None)
    
    def test_str(self):
        node = TextNode("test", "bold", "a url")
        node2 = TextNode("test", "bold")

        self.assertEqual(node.__repr__(), "TextNode(test, bold, a url)")
        self.assertEqual(node2.__repr__(), "TextNode(test, bold, None)")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("text value", TextType.TEXT)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "text value")

    def test_bold(self):
        node = TextNode("bold value", TextType.BOLD)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "bold value")

    def test_img(self):
        node = TextNode("img value", TextType.IMAGE, "https://test")
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertAlmostEqual(
            html.props,
            {"src": "https://test", "alt": "img value"}
        )

    def test_error(self):
        node = TextNode("error", "bob")

        with self.assertRaises(ValueError) as err:
            text_node_to_html_node(node)
        
        # Check if the exception message is correct
        self.assertEqual(str(err.exception), "bob is invalid")

if __name__ == "__main__":
    unittest.main()