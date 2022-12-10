lines = open("input.txt", "r").read().split("\n")

reg_values = {}
cycles = 0
x_reg = 1

def register_cycle(cycle, register_val):
    global reg_values

    if (cycle == 20):
        reg_values[str(cycle)] = int(register_val)
    elif (cycle > 20):
        c = cycle
        c -= 20
        if (c % 40 == 0):
            reg_values[str(cycle)] = int(register_val)


for l in lines:
    args = l.split(" ")

    if (args[0] == "noop"):
        cycles += 1
        register_cycle(cycles, x_reg)    

    elif (args[0] == "addx"):
        cycles += 1
        register_cycle(cycles, x_reg)
        cycles += 1
        register_cycle(cycles, x_reg)
        x_reg += int(args[1])      

sum = 0
for key in reg_values.keys():
    c = int(key)
    r = int(reg_values[key])
    t = c * r
    sum += t
print ("Part 1: " + str(sum))