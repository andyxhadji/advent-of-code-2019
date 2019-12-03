# https://adventofcode.com/2019/day/2

OPERATIONS = { 1: lambda x, y: x + y, 2: lambda x, y: x * y }
GOAL = 19690720

def fix_intcode():
    f = open('input.txt', 'r')
    intcode = f.read()
    intcode_list = intcode.split(",")
    intcode_list = list(map(int, intcode_list))

    # Initialize position 1 and 2 to start at zero, save copy
    position_1, position_2 = 0, 0
    intcode_list[1], intcode_list[2] = position_1, position_2
    original_list = intcode_list.copy()
    
    # Start iterating position 1 until near goal
    while run_intcode_ops(intcode_list) <= (GOAL - 99):
        position_1 += 1
        intcode_list = original_list.copy()
        intcode_list[1] = position_1

    # Now iterate position 2 until hits goal
    # Save copy of opcode with solved position 1
    position_1_list = original_list.copy() 
    position_1_list[1] = position_1
    position_1_list_original = position_1_list.copy()
    
    while run_intcode_ops(intcode_list) != GOAL:
        position_2 += 1
        intcode_list = position_1_list_original.copy()
        intcode_list[2] = position_2

    return position_1, position_2


def run_intcode_ops(intcode_list):
    for count in range(0, len(intcode_list), 4):
        if intcode_list[count] not in [1, 2]:
            break
        else: 
            position_1, position_2 = intcode_list[count + 1], intcode_list[count + 2]
            new_amount = OPERATIONS[intcode_list[count]](intcode_list[position_1], intcode_list[position_2])
            intcode_list[intcode_list[count + 3]] = new_amount
    return intcode_list[0]


print(fix_intcode())
