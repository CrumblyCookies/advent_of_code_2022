import constant
lines = open("input.txt", "r").read().split("\n")


def calc_line_score(line):
    repeated = find_dupe(line)
    return calc_letter_score(repeated)


def find_dupe(line):
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for i in range(0, len(firstpart)):
        if (secondpart[i] in firstpart):
            return secondpart[i]  
    return "\0"


def calc_letter_score(letter):
    return constant.SCORE.index(letter)


score = 0
for l in lines:
    score += calc_line_score(l)
print (score)