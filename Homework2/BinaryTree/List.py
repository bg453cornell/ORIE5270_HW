class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.value = next_node


class List(object):
    def __init__(self, node):
        self.first = node

    def add(self, value):
        node = Node(value)
        current_node = self.first
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop(self):
        value = self.last.value

def find_negative_cycles(name_txt_file)
    #use:bellman-ford alg.

def find_shortest_path(name_txt_file, source, destination)
    #use: Dijkstra's algorithm, you can use a library includes a priority queue