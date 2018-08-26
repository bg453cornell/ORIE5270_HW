class Tree(object):
    def __init__(self, root):
        """

        :param root: (Node) root node
        """
        self.root = root

    def get_depth(self, node):
        """

        :param node: (Node) root node
        :return: (int) depth of the tree
        """
        if node is not None:
            if node.left is None and node.right is None:
                return 1
            return 1 + max(self.get_depth(node.left), self.get_depth(node.right))
        return 0

    def build_tree(self, depth):
        """

        :param depth: (int) depth of the tree
        :return: (list of lists) all nodes in the tree,
                nodes on the same level stored in the same list
        """
        tree_list = []
        if self.root is not None:
            current_level = [self.root]
            tree_list.append(current_level)
            for i in range(1, depth):
                next_level = [None] * (2 ** i)
                for idx in range(len(current_level)):
                    if current_level[idx] is not None:
                        next_level[2*idx] = current_level[idx].left
                        next_level[2*idx+1] = current_level[idx].right
                current_level = next_level
                tree_list.append(current_level)
        return tree_list

    @property
    def print_tree(self):
        """

        :return: (list of lists) output of the tree, empty places filled with '|'
        """
        depth = self.get_depth(self.root)
        tree_list = self.build_tree(depth)
        tree = [["|" for j in range(2**depth-1)] for i in range(depth)]
        tmp_list = list(reversed(tree_list))
        for i, level in enumerate(tmp_list):
            for j, node in enumerate(level):
                if node is not None:
                    row = depth - i - 1
                    col = 2**i - 1 + j*(2**(i + 1))
                    tree[row][col] = str(node.value)
        for level in tree:
            print(''.join(level))
        return tree
