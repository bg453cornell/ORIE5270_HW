from BinaryTree.Tree import Tree
from BinaryTree.Node import Node

if __name__ == '__main__':
    root1 = Node(1, Node(2, Node(4, Node(5), Node(9)), Node(3, Node(4), Node(5))), Node(3, Node(5, Node(2), Node(4)),
                                                                                        Node(6, Node(1), Node(5))))
    # tree1 = Tree(root1)
    # depth = tree1.get_depth(tree1.root)
    # print(depth)
    # print(tree.build_tree(depth))
    # tree_list = tree1.build_tree(depth)
    # tree1.print_tree(depth, tree_list)
    # tree.print_tree()

    root2 = Node(1, None, Node(2, Node(3), Node(4)))
    tree2 = Tree(root2)
    tree2.print_tree
