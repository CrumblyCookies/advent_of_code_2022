lines = open("input.txt", "r").read().split("\n")

# Grid is [y][x] indexed
def build_grid():
    g = []
    for i in range(0, len(lines)):
        g.append([])

    for i in range(0, len(lines)):
        for c in lines[i]:
            g[i].append(int(c))
            
    return g


def calc_dir(y, x, y_delta, x_delta, grid):
    val = grid[y][x]
    check_x = x + x_delta
    check_y = y + y_delta
    trees_seen = 0

    while is_coordinate_inbound(check_x, check_y, grid):
        trees_seen += 1     
        if (grid[check_y][check_x] >= val):
            return (False, trees_seen)    
        check_x += x_delta
        check_y += y_delta        

    return (True, trees_seen)
        

def is_coordinate_inbound(x, y, grid):
    x_in = x >= 0 and x <= len(grid[0]) - 1
    y_in = y >= 0 and y <= len(grid) - 1
    return x_in and y_in
    

def check_tree(y, x, grid):
    up = calc_dir(y, x, -1, 0, grid)
    right = calc_dir(y, x, 0, 1, grid)
    down = calc_dir(y, x, 1, 0, grid)
    left = calc_dir(y, x, 0, -1, grid)

    visible = up[0] or right[0] or down[0] or left[0]
    score = up[1] * right[1] * down[1] * left[1]

    return (visible, score)


# Start
grid = build_grid()
hei = len(lines)
wid = len(lines[0])

# Part 1
visible_count = 0
for y in range(1, hei - 1):
    for x in range(1, wid - 1):
        is_visible = check_tree(y, x, grid)[0]
        if (is_visible):
            visible_count += 1

# Calc outside amounts
top = len(lines[0])
bot = top
left = len(lines) - 2
right = left
visible_count += top + bot + left + right
print ("Part 1: " + str(visible_count))


# Part 2
highest_scenic_score = 0
for y in range(0, hei):
    for x in range(0, wid):
        score = check_tree(y, x, grid)[1]
        if (score > highest_scenic_score):
            highest_scenic_score = score
print ("Part 2: " + str(highest_scenic_score))
