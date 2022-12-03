lines= open("input.txt", "r").read().split("\n")

score = 0

def calc_score(play, response):
    round_score = 0
    if (response == "X"):
        round_score += get_losing_response(play)
    elif (response == "Y"):
        round_score += 3
        round_score += get_drawing_response(play)
    elif (response == "Z"):
        round_score += 6
        round_score += get_winning_response(play)
    return round_score


def get_losing_response(shape):
    if (shape == "A"):
        return 3
    if (shape == "B"):
        return 1
    if (shape == "C"):
        return 2
    return 0


def get_drawing_response(shape):
    if (shape == "A"):
        return 1
    if (shape == "B"):
        return 2
    if (shape == "C"):
        return 3
    return 0


def get_winning_response(shape):
    if (shape == "A"):
        return 2
    if (shape == "B"):
        return 3
    if (shape == "C"):
        return 1
    return 0


for l in lines:
    shapes = l.split(" ")
    weee = calc_score(shapes[0], shapes[1])
    print("" + shapes[0] + " " + shapes[1] + " = " + str(weee))
    score += calc_score(shapes[0], shapes[1])

print ("Score: " + str(score))