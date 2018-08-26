class Node(object):
    def __init__(self, value, left=None, right=None):
        """

        :param value: (int) value of the node
        :param left:  (Node) left node
        :param right: (Node) right node
        """
        self.value = value
        self.left = left
        self.right = right
