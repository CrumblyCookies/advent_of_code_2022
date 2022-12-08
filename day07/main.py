from directory import Directory
from directory import File

lines = open("input.txt", "r").read().split("\n")

# Make root
current_directory = Directory("/", None)


# Parse input, build the fs
for l in lines:
    if (l == "$ cd /"):
        continue
    
    args = l.split(" ")

    # Command
    if (args[0] == "$"):
        match args[1]:
            case "cd":
                if (args[2] == ".."):
                    current_directory = current_directory.get_parent()
                else:
                    current_directory = current_directory.get_directory(args[2])               
            case "ls":
                continue

    # Parsing dir
    if (args[0] == "dir"):
        current_directory.add_directory(args[1])
    elif (args[0].isnumeric()):
        file_size = int(args[0])
        file_name = str(args[1])
        current_directory.add_file(File(file_name, file_size))


# Return to parent
while (current_directory.get_parent() is not None):
    current_directory = current_directory.get_parent()


# Part 1
dir_list = []
current_directory.gather_all_under_given_size(100000, dir_list)
total = 0
for d in dir_list:
    total += d.get_total_size()
print("Part 1: " + str(total))


# Part 2
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
current_used_space = current_directory.get_total_size()
current_space_remaining = TOTAL_SPACE - current_used_space
need_to_delete = REQUIRED_SPACE - current_space_remaining
dir_list = []
current_directory.gather_all_over_given_size(need_to_delete, dir_list)
current_smallest = current_directory.get_total_size()
current_smallest_name = current_directory.name
for d in dir_list:
    if (d.get_total_size() < current_smallest):
        current_smallest = d.get_total_size()
        current_smallest_name = d.name
print("Part 2: " + str(current_smallest))
