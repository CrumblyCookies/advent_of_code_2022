lines_split = open("input.txt", "r").read().split("\n")

max_calories = 0
top_three = [0, 0, 0]
current_calories = 0

for l in lines_split:

    if not l:

        if (current_calories > max_calories):
            max_calories = current_calories

        # Slow and inefficient but simple
        top_three.append(current_calories)
        top_three.sort()
        top_three.pop(0)
       
        current_calories = 0
        
    else:

        calories = int(l)
        current_calories += calories

print("Ans 1: " + str(max_calories) + " Ans 2: " + str(sum(top_three)))