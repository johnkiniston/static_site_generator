from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # tag and children are required positional arguments
        # value is explicitly passed as None to the parent constructor
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("Invalid HTML: ParentNode must have children.")
        
        # Recursively build the HTML string for all children
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
            
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
