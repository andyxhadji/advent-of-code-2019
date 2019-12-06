# https://adventofcode.com/2019/day/3

OPERATIONS = { 'R': lambda x, y, z: (x + z, y),
               'U': lambda x, y, z: (x, y + z),
               'L': lambda x, y, z: (x - z, y),
               'D': lambda x, y, z: (x, y - z),
             }

def get_coords_from_to(start, movement, path_length) -> list:
    # returns all coordinate steps to get to final destination (right inclusive)
    direction, distance = movement[0], int(movement[1:])
    if distance == 0:
        return []
    begin_path_length = path_length[start]
    all_steps = []

    for steps in range(1, distance+1):
        new_step = OPERATIONS[direction](start[0], start[1], steps)
        all_steps.append(new_step)
        path_length[new_step] = begin_path_length + steps
    
    return all_steps

def get_shortest_manhattan_distance(shared_coords):
    # find distance from (0, 0) for each point, return shortest distance
    return min([abs(coord[0]) + abs(coord[1]) for coord in shared_coords])

def get_shortest_path_to_intersection(shared_coords, wire1_path_length, wire2_path_length):
    # find shortest distance of wires for all intersections
    return min([wire1_path_length[coord] + wire2_path_length[coord] for coord in shared_coords])

def find_wire_intersection_paths():
    f = open("input.txt", "r")
    wires = []
    for line in f:
        wires.append(line.rstrip('\n').split(","))
    
    coords = {0: set(), 1: set()}
    path_lengths = {0: {(0, 0): 0}, 1: {(0, 0): 0}}
    wire2_start = (0, 0)
    for count in range(0, len(wires)):
        wire = wires[count]
        wire_start = (0, 0)
        for movement in wire:
            # Get all coordinates from start to end
            # Keep track of amount of wire needed for each coordinate (path_lengths)
            path = get_coords_from_to(wire_start, movement, path_lengths[count])
            wire_start = path[-1]
            for coord in path:
                coords[count].add(coord)

    coord_intersection = coords[0].intersection(coords[1])
    # return get_shortest_manhattan_distance(coord_intersection)
    return get_shortest_path_to_intersection(coord_intersection, path_lengths[0], path_lengths[1])
        

print(find_wire_intersection_paths())
