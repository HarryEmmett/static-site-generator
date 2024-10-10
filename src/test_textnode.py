import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()