lines = open("input.txt", "r").read().split("\n")

class Assignment:

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def does_contain(self, check):
        return (self.lower <= check.lower and self.upper >= check.upper)

    def does_overlap(self, check):
        return self.does_contain_number(check.lower) or self.does_contain_number(check.upper)

    def does_contain_number(self, num):
        return (self.lower <= num and self.upper >= num)


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def is_contained(self):
        return self.first.does_contain(self.second) or self.second.does_contain(self.first)

    def is_overlap(self):
        return self.first.does_overlap(self.second) or self.second.does_overlap(self.first)

    def to_string(self):
        return "" + str(self.first.lower) + "-" + str(self.first.upper) + "," + str(self.second.lower) + "-" + str(self.second.upper)


pairs = []
for line in lines:
    assignments = line.split(",")
    first_a = assignments[0].split("-")
    second_a = assignments[1].split("-")
    A = Assignment(int(first_a[0]), int(first_a[1]))
    B = Assignment(int(second_a[0]), int(second_a[1]))
    P = Pair(A, B)
    pairs.append(P)


num_containing = 0
for pair in pairs:
    if (pair.is_contained()):
        num_containing += 1

print ("Part 1: " + str(num_containing))

num_overlapping = 0
for pair in pairs:
    if (pair.is_overlap()):
        num_overlapping += 1

print ("Part 2: " + str(num_overlapping))