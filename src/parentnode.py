from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag property")
        if self.children is None:
            raise ValueError("No children property")
        
        str = ""
        for child in self.children:
            str += child.to_html()

        return f"<{self.tag}>{str}</{self.tag}>"