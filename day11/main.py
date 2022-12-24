from monkey import Monkey
from monkey import Operation
from monkey import OperationTarget

lines = open("input.txt", "r").read().split("\n")

DIVISION_VALUE = 3
ROUND_COUNT = 20
MORE_ROUND_COUNT = 1000

def parse_monkeys():
    monkey_list = []
    current_monkey = None

    for l in lines:

        if ("Monkey" in l):
            if (current_monkey is not None):
                monkey_list.append(current_monkey)
            current_monkey = Monkey()

        if ("Starting" in l):
            args = l.split(":")
            nums = args[1].split(",")
            for i in range(0, len(nums)):
                current_monkey.current_items.append(nums[i].strip())

        if ("Operation" in l):
            args = l.split("=")
            op = "*" if ("*" in args[1]) else "+"
            current_monkey.operation = Operation.MULTIPLY if (op == "*") else Operation.ADD
            op_target = args[1].split(op)[1].strip()
            if (op_target == "old"):
                current_monkey.operation_target_type = OperationTarget.OLD_VALUE
            else:
                current_monkey.operation_target_type = OperationTarget.LITERAL
                current_monkey.operation_literal_value = int(op_target)

        if ("Test" in l):
            current_monkey.division_test = int(l.split("by")[1].strip())

        if ("true" in l):
            current_monkey.true_throw = int(l.split("monkey")[1].strip())
        
        if ("false" in l):
            current_monkey.false_throw = int(l.split("monkey")[1].strip())

    monkey_list.append(current_monkey)
    return monkey_list


def perform_round(monkey_list, should_divide):

    for i in range(0, len(monkey_list)):
 
        while (len(monkey_list[i].current_items) > 0):

            # Count
            monkey_list[i].inspection_count += 1

            # Get item to inspect
            item = int(monkey_list[i].current_items.pop(0))

            # Perform operation
            adjust_by = int(monkey_list[i].operation_literal_value) if (monkey_list[i].operation_target_type == OperationTarget.LITERAL) else item
            if (monkey_list[i].operation == Operation.MULTIPLY):
                item *= adjust_by
            else:
                item += adjust_by

            # Divide
            if (should_divide):
                item /= DIVISION_VALUE
                item = int(item)

            # Test
            if (item % int(monkey_list[i].division_test) == 0):
                monkey_list[int(monkey_list[i].true_throw)].current_items.append(item)
            else:
                monkey_list[int(monkey_list[i].false_throw)].current_items.append(item)


# Part 1
monkeys = parse_monkeys()
for i in range(0, ROUND_COUNT):
    perform_round(monkeys, True)
monkeys.sort()
monkey_business = monkeys[0].inspection_count * monkeys[1].inspection_count
print("Part 1: " + str(monkey_business))


# Part 2
# more_monkeys = parse_monkeys()
# for i in range(0, MORE_ROUND_COUNT):
#     print(i)
#     perform_round(more_monkeys, False)

# more_monkeys.sort()
# more_monkey_business = more_monkeys[0].inspection_count * more_monkeys[1].inspection_count
# print("Part 2: " + str(more_monkey_business))