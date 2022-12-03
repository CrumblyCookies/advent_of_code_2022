import constant
lines = open("input.txt", "r").read().split("\n")


def calc_rucksack(a, b, c):
    repeated = find_dupe(a, b, c)
    return calc_letter_score(repeated)


def find_dupe(a, b, c):
    letter_dict = {}
    for i in range(1, len(constant.SCORE)):
        letter_dict[constant.SCORE[i]] = 0

    populate_dict_with_line(letter_dict, a)
    populate_dict_with_line(letter_dict, b)
    populate_dict_with_line(letter_dict, c)

    for letter in letter_dict.keys():
        if (letter_dict[letter] == 3):
            return letter   
    return "\0"


def populate_dict_with_line(dict, line):
    without_dupes = "".join(set(line))
    for i in range(0, len(without_dupes)):
        dict[without_dupes[i]] += 1


def calc_letter_score(letter):
    return constant.SCORE.index(letter)


score = 0
rucksack = []
for l in lines:
    rucksack.append(l)
    if (len(rucksack) == 3):
        score += calc_rucksack(rucksack[0], rucksack[1], rucksack[2])
        rucksack.clear()


print (score)