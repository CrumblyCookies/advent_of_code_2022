from enum import Enum

class Operation(Enum):
    NONE = 0
    MULTIPLY = 1
    ADD = 2

class OperationTarget(Enum):
    NONE = 0
    LITERAL = 1
    OLD_VALUE = 2

class Monkey:

    def __init__(self):
        self.inspection_count = 0
        self.current_items = []
        self.operation = Operation.NONE
        self.operation_target_type = OperationTarget.NONE
        self.operation_literal_value = 0
        self.division_test = 0
        self.true_throw = 0
        self.false_throw = 0

    def __lt__(self, other):
         return self.inspection_count > other.inspection_count