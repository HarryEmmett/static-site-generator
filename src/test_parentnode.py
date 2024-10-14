import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_str(self):
        node = ParentNode("tag", "value", "props")
        node2 = ParentNode("tag1", "value1")

        self.assertEqual(node.__repr__(), "ParentNode(tag, children: value, props)")
        self.assertEqual(node2.__repr__(), "ParentNode(tag1, children: value1, None)")

    def many_children(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            )

if __name__ == "__main__":
    unittest.main()