import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_url(self):
        node = TextNode("this is text", TextType.PLAIN, None)
        node2 = TextNode("this is text", TextType.PLAIN, )
        self.assertEqual(node, node2)
    def test_texttype(self):
        node = TextNode("this is text", TextType.LINKS)
        node2 = TextNode("this is text", TextType.BOLD)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()