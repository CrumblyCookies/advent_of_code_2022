class Node:

    def __init__(self, id, val, x, y):
        self.id = id
        self.value = val
        self.x = x
        self.y = y

        # A*
        self.f = 0
        self.h = 0
        self.g = 0
        self.children = []
        self.parent = None