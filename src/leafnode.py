from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Enforce no children by explicitly passing None for the children argument
        # tag and value are required positional arguments
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag is None:
            return self.value
            
        # Inherit props_to_html from the parent HTMLNode class
        props_str = self.props_to_html() 
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        # Override __repr__ to omit children, matching this class's structure
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
