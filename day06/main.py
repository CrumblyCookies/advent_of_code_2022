line = open("input.txt", "r").read()


FIRST_TEST_LENGTH = 4
SECOND_TEST_LENGTH = 14


def check_string_uniqueness(str):
    new_string = "".join(set(str))
    return len(str) == len(new_string)


def get_som_marker_end_index(data, length):

    for i in range(0, len(data)):

        test_string = data[i]

        for j in range(1, length):
            test_string += data[i + j]

        if (check_string_uniqueness(test_string)):
            return i + length


print("Part 1: " + str(get_som_marker_end_index(line, FIRST_TEST_LENGTH)))
print("Part 2: " + str(get_som_marker_end_index(line, SECOND_TEST_LENGTH)))