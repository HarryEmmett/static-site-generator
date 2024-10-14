import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "test", None, {"test_a": "a_value", "test_b": "b_value"})
        self.assertEqual(
            node.props_to_html(),
            " test_a='a_value' test_b='b_value'"
        )

    def test_none_props(self):
        node = HTMLNode()

        self.assertEqual(
            node.tag, None
        )
        self.assertEqual(
            node.value, None
        )
        self.assertEqual(
            node.children, None
        )
        self.assertEqual(
            node.props, None
        )

    def test_value_props(self):
        node = HTMLNode("a", "b", "c", {})

        self.assertEqual(
            node.tag, "a"
        )
        self.assertEqual(
            node.value, "b"
        )
        self.assertEqual(
            node.children, "c"
        )
        self.assertEqual(
            node.props, {}
        )   

    def test_repr(self):
        node = HTMLNode("a", "b", "c", {})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, b, c, {})"
        )  

if __name__ == "__main__":
    unittest.main()