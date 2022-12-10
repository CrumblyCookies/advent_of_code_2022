lines = open("input.txt", "r").read().split("\n")

current_cycle = 0
x_reg = 1

current_row = 0
current_column = 0
screen = {}

def register_sprite():
    global current_cycle
    global x_reg
    global current_row
    global current_column
    global screen

    # The row of the screen we're on
    if (current_cycle % 40 == 0):
        row = int(current_cycle / 40) - 1
    else:
        row = int(current_cycle / 40)

    # Make new screen row if needed
    if (not row in screen.keys()):
        screen[row] = []
    
    # The column of the screen we're on
    column = current_cycle
    while (column > 40):
        column -= 40

    # Determine if pixel is visible
    visible = (column >= x_reg and column <= (x_reg + 2))
    pixel = "#" if visible else "."

    # Add
    screen[row].append(pixel)


for l in lines:
    args = l.split(" ")

    if (args[0] == "noop"):
        current_cycle += 1
        register_sprite()

    elif (args[0] == "addx"):
        current_cycle += 1
        register_sprite()
        current_cycle += 1
        register_sprite()
        x_reg += int(args[1])


# Build strings for outputting
strings = []
for key in screen.keys():
    output = ""
    for c in screen[key]:
        output += c
    print (output)