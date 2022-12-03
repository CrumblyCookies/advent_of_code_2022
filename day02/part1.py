lines= open("input.txt", "r").read().split("\n")

score = 0

def calc_score(play, response):
    shape_score = get_score_for_shape(response)
    win_score = calc_win_score(play, response)
    return shape_score + win_score


def calc_win_score(play, response):  
    if (is_shape_same(play, response)):
        return 3
    if (play == "A"):
        return 6 if response == "Y" else 0
    elif (play == "B"):
        return 6 if response == "Z" else 0
    elif (play == "C"):
        return 6 if response == "X" else 0
    return 0


def get_score_for_shape(shape):
    if (shape == "X"):
        return 1
    elif (shape == "Y"):
        return 2
    elif (shape == "Z"):
        return 3
    else:
        return 0


def is_shape_same(play, response):
    if (play == "A"):
        return (response == "X")
    elif (play == "B"):
        return (response == "Y")
    elif (play == "C"):
        return (response == "Z")
    return False


for l in lines:
    shapes = l.split(" ")
    score += calc_score(shapes[0], shapes[1])


print ("Score: " + str(score))