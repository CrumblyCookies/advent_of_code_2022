from collections import deque

class StackManager:

    def __init__(self):
        self.stacks = {}

    def get_stack(self, key):
        str_key = str(key)
        if (not str_key in self.stacks.keys()):
            self.create_stack_with_key(key)
        return self.stacks[str_key]

    def create_stack_with_key(self, key):
        str_key = str(key)
        self.stacks[str_key] = Stack()

    def print(self):
        for key in sorted(self.stacks.keys()):
            print (key + " " + str(self.stacks[key].stack))

    def stack_tops_to_string(self):
        ans = ""
        for key in sorted(self.stacks.keys()):
            ans += self.stacks[key].stack[-1]
        return ans


class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, obj):
        self.stack.append(obj)

    def put_at_front(self, obj):
        self.stack.appendleft(obj)

    def pop(self):
        return self.stack.pop()