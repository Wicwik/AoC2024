import numpy as np
from copy import deepcopy

sit_map = []
start_pos = ()

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        sit_map.append(list(line.strip()))

        if "^" in line:
            start_pos = (i, line.find("^"))

def find_nearest_hash_to_left(lst, index, pos):
    for i in range(index - 1, -1, -1):
        if lst[i] == "#":
            return i

    return None

def find_nearest_hash_to_right(lst, index, pos):
    for i in range(index, len(lst)):
        if lst[i] == "#":
            return i
        
    return None 


def check_loop(start_pos, start_rotation):
    cur_pos = start_pos

    i = 0

    while True:
        i += 1

        if sit_map[cur_pos[0]][cur_pos[1]] == "^":
            crate_pos = find_nearest_hash_to_left(np.array(sit_map)[:, cur_pos[1]], cur_pos[0], cur_pos[1])

            sit_map[cur_pos[0]][cur_pos[1]] = "."

            if crate_pos == None:
                return False

            cur_pos = (cur_pos[0] - (cur_pos[0] - crate_pos - 1), cur_pos[1])

            sit_map[cur_pos[0]][cur_pos[1]] = ">"

        elif sit_map[cur_pos[0]][cur_pos[1]] == "v":
            crate_pos = find_nearest_hash_to_right(np.array(sit_map)[:, cur_pos[1]], cur_pos[0], cur_pos[1])

            sit_map[cur_pos[0]][cur_pos[1]] = "."

            if crate_pos == None:
                return False

            cur_pos = (cur_pos[0] + (crate_pos - cur_pos[0] - 1),  cur_pos[1])

            sit_map[cur_pos[0]][cur_pos[1]] = "<"

        elif sit_map[cur_pos[0]][cur_pos[1]] == ">":
            crate_pos = find_nearest_hash_to_right(sit_map[cur_pos[0]], cur_pos[1], cur_pos[0])

            sit_map[cur_pos[0]][cur_pos[1]] = "."

            if crate_pos == None:
                return False

            cur_pos = (cur_pos[0],  cur_pos[1] + (crate_pos - cur_pos[1] - 1))

            sit_map[cur_pos[0]][cur_pos[1]] = "v"

            
        elif sit_map[cur_pos[0]][cur_pos[1]] == "<":
            crate_pos = find_nearest_hash_to_left(sit_map[cur_pos[0]], cur_pos[1], cur_pos[0])

            sit_map[cur_pos[0]][cur_pos[1]] = "."

            if crate_pos == None:
                return False

            cur_pos = (cur_pos[0], cur_pos[1] - (cur_pos[1] - crate_pos - 1))

            sit_map[cur_pos[0]][cur_pos[1]] = "^"

        if i > 1000:
            return True

        if start_pos[0] == cur_pos[0] and start_pos[1] == cur_pos[1] and start_rotation == sit_map[cur_pos[0]][cur_pos[1]]:
            return True

        


n_loops = 0
start_sit_map = deepcopy(sit_map)

# brute force
for i in range(len(sit_map)):
    for j in range(len(sit_map[0])):
        sit_map = deepcopy(start_sit_map)

        if i == start_pos[0] and j == start_pos[1]:
            continue
        
        sit_map[i][j] = "#" # add obstacle

        if check_loop(start_pos, "^"):
            n_loops += 1



print(n_loops)