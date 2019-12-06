# https://adventofcode.com/2019/day/4

def check_two_same_adjacent(first_index, second_index, password):
    if password[first_index] == password[second_index]:
        digit = password[first_index]
        left_surrounding = first_index - 1
        if left_surrounding >= 0:
            if password[left_surrounding] == digit:
                return False

        right_surrounding = second_index + 1
        if right_surrounding < len(password):
            if password[right_surrounding] == digit:
                return False
        return True
    return False

def check_decreasing(first, second):
    return first <= second

def rule_checker(password):
    two_same_adjacent = False
    for count in range(0, len(password) - 1):
        first_int, second_int = int(password[count]), int(password[count + 1])
        if check_two_same_adjacent(count, count + 1, password):
            two_same_adjacent = True
        if not check_decreasing(first_int, second_int):
            return False

    return two_same_adjacent

def find_potential_password_count():
    input_nums = "152085-670283"
    begin, end = input_nums.split("-")
    count = 0
    for candidate in range(int(begin), int(end) + 1):
        if rule_checker(str(candidate)):
            count += 1

    return count


print(find_potential_password_count())
