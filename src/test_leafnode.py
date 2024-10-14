import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_str(self):
        node = LeafNode("tag", "value", "props")
        node2 = LeafNode("tag1", "value1")

        self.assertEqual(node.__repr__(), "LeafNode(tag, value, props)")
        self.assertEqual(node2.__repr__(), "LeafNode(tag1, value1, None)")
    
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode(None, "No tag!")

        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), "<a href='https://www.google.com'>Click me!</a>")
        self.assertEqual(node3.to_html(), "No tag!")

if __name__ == "__main__":
    unittest.main()