from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        if url == None:
            self.url = None
        else:
            self.url = url
    def __eq__(self, text_Node):
        if self.text == text_Node.text:
            if self.text_type == text_Node.text_type:
                if self.url == text_Node.url:
                    return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"