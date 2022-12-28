from node import Node

class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, n):
        self.nodes.append(n)

    def get_node_by_pos(self, x, y):
        for n in self.nodes:
            if (n.x == x and n.y == y):
                return Node(n.id, n.value, n.x, n.y)
        return None

    def get_node_by_val(self, val):
        for n in self.nodes:
            if (n.value == val):
                return Node(n.id, n.value, n.x, n.y)
        return None