from enum import Enum
import copy
import stackmanager
import constants

lines = open("input.txt", "r").read().split("\n")

class ParseMode(Enum):
    CRATE = 0
    INSTRUCTIONS = 1

stack_manager_original = stackmanager.StackManager()
stack_manager_modified = stackmanager.StackManager()
mode = ParseMode.CRATE

for l in lines:

    if (mode == ParseMode.CRATE):

        if (l == ""):
            mode = ParseMode.INSTRUCTIONS
            stack_manager_modified = copy.deepcopy(stack_manager_original)
            continue

        column = 0
        for i in range(0, len(l), constants.COL_WID):
            if (l[i] == "["):
                crate = l[i+1]
                index = column + 1
                stack_manager_original.get_stack(index).put_at_front(crate)
            column += 1

    elif (mode == ParseMode.INSTRUCTIONS):
        
        instructions = l.split(" ")
        amount_to_move = int(instructions[1])
        move_from = instructions[3]
        move_to = instructions[5]

        # Part 1
        for i in range(0, amount_to_move):
            crate = stack_manager_original.get_stack(move_from).pop()
            stack_manager_original.get_stack(move_to).push(crate)

        # Part 2
        crates = ""
        for i in range(0, amount_to_move):
            crate = stack_manager_modified.get_stack(move_from).pop()
            crates += crate
        reversed_c = crates[::-1]
        for c in reversed_c:
            stack_manager_modified.get_stack(move_to).push(c)


print ("Part 1: " + stack_manager_original.stack_tops_to_string())
print ("Part 2: " + stack_manager_modified.stack_tops_to_string())