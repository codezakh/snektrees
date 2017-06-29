import unittest
from tree import Node


class NodeTestCase(unittest.TestCase):
    def test_create_triangle(self):
        root_node = Node(data='a')
        left_node = root_node.add_left(data='b')
        right_node = root_node.add_right(data='c')
        self.assertIs(left_node.parent, right_node.parent)
        self.assertIs(left_node.sibling, right_node)
        self.assertIs(right_node.sibling, left_node)
        self.assertIs(root_node.right, right_node)
        self.assertIs(root_node.left, left_node)


class TreeTestCase(unittest.TestCase):

    def test_creating_tree(self):
        _tree = Node.mktree(range(7))
        self.assertEqual(_tree.inorder(), range(7))

    def test_postorder_traversal(self):
        _tree = Node.mktree([1,2,3,4,5])
        self.assertEqual(_tree.postorder(), [5,4,3,2,1])

    def test_preorder_traversal(self):
        _tree = Node.mktree([1,2,3,4,5,11,7])
        self.assertEqual(_tree.preorder(), [1,2,3,4,5,11,7])

    def test_sexp(self):
        _tree = Node.mktree([1,2,3,4,5,11,7])
        self.fail(_tree.sexp())

if __name__ == "__main__":
	unittest.main()
