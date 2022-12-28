import math

class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def dist(left, right):
        diff_x = left.x - right.x
        diff_y = left.y - right.y
        return math.sqrt((diff_x * diff_x + diff_y * diff_y))