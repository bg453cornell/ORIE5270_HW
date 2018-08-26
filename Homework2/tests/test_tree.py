import unittest
from BinaryTree.Tree import Tree
from BinaryTree.Node import Node


class TestTree(unittest.TestCase):

    def test_tree_1(self):
        node1 = Node(1)
        tree = Tree(node1)
        assert tree.print_tree == [['1']]

    def test_tree_2(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.left = node2
        node1.right = node3
        tree = Tree(node1)
        assert tree.print_tree == [['|', '1', '|'],
                                   ['2', '|', '3']]

    def test_tree_3(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.left = node2
        node2.left = node3
        tree = Tree(node1)
        assert tree.print_tree == [['|', '|', '|', '1', '|', '|', '|'],
                                   ['|', '2', '|', '|', '|', '|', '|'],
                                   ['3', '|', '|', '|', '|', '|', '|']]

    def test_tree_4(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.right = node2
        node2.left = node3
        node2.right = node4
        tree = Tree(node1)
        assert tree.print_tree == [['|', '|', '|', '1', '|', '|', '|'],
                                   ['|', '|', '|', '|', '|', '2', '|'],
                                   ['|', '|', '|', '|', '3', '|', '4']]
