import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "test", None, {"test_a": "a_value", "test_b": "b_value"})
        self.assertEquals(
            node.props_to_html(),
            " test_a='a_value' test_b='b_value'"
        )

    def test_none_props(self):
        node = HTMLNode()

        self.assertEquals(
            node.tag, None
        )
        self.assertEquals(
            node.value, None
        )
        self.assertEquals(
            node.children, None
        )
        self.assertEquals(
            node.props, None
        )

    def test_value_props(self):
        node = HTMLNode("a", "b", "c", {})

        self.assertEquals(
            node.tag, "a"
        )
        self.assertEquals(
            node.value, "b"
        )
        self.assertEquals(
            node.children, "c"
        )
        self.assertEquals(
            node.props, {}
        )   

    def test_repr(self):
        node = HTMLNode("a", "b", "c", {})
        self.assertEquals(
            node.__repr__(),
            "HTMLNode(a, b, c, {})"
        )  

if __name__ == "__main__":
    unittest.main()