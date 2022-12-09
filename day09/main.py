lines = open("input.txt", "r").read().split("\n")

x = "x"
y = "y"

def move_head(head, move_dir):
    global x
    global y
    
    match move_dir:
        case "U":
            head[y] += 1
        case "R":
            head[x] += 1
        case "D":
            head[y] -= 1
        case "L":
            head [x] -= 1
    return head


def catch_up(tail, head):
    global x
    global y

    x_dif = head[x] - tail[x]
    y_dif = head[y] - tail[y]
    total_dist = abs( abs(x_dif) + abs(y_dif))
    x_move = 0
    y_move = 0

    # Diagonal
    if (total_dist > 2):  
        x_move = 1 if (head[x] > tail[x]) else -1
        y_move = 1 if (head[y] > tail[y]) else -1      
    else:
        if (abs(x_dif) == 2):
            x_move = 1 if (head[x] > tail[x]) else -1
        if (abs(y_dif) == 2):
            y_move = 1 if (head[y] > tail[y]) else -1

    tail[x] += x_move
    tail[y] += y_move

    return tail


# Part 1
h = {x:0, y:0}
t = {x:0, y:0}
dirty_tiles = {}
for l in lines:
    args = l.split(" ")
    num = int(args[1])
    for i in range(0, num):
        h = move_head(h, args[0])
        t = catch_up(t, h)
        key = str(t[x]) + "_" + str(t[y])
        dirty_tiles[key] = True
    
print ("Part 1: " + str(len(dirty_tiles.keys())))


# Part 2
rope = []
ROPE_LEN = 10
for i in range(0, ROPE_LEN):
    rope.append({x:0, y:0})

dirty_tiles = {}
for l in lines:
    args = l.split(" ")
    num = int(args[1])
    for i in range(0, num):

        rope[0] = move_head(rope[0], args[0])

        for i in range(1, len(rope)):
            rope[i] = catch_up(rope[i], rope[i-1])

        key = str(rope[ROPE_LEN-1][x]) + "_" + str(rope[ROPE_LEN-1][y])
        dirty_tiles[key] = True
    
print("Part 2: " + str(len(dirty_tiles.keys())))
