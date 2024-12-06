import numpy as np

sit_map = []
start_pos = ()

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        sit_map.append(list(line.strip()))

        if "^" in line:
            start_pos = (i, line.find("^"))

print(start_pos)

def find_nearest_hash_to_left(lst, index, pos):
    for i in range(index - 1, -1, -1):
        if lst[i] == "#":
            return i
        
        if type(lst) == np.ndarray:
            sit_map[i][pos] = "X"
        else:
            sit_map[pos][i] = "X"

    return None

def find_nearest_hash_to_right(lst, index, pos):
    for i in range(index, len(lst)):
        if lst[i] == "#":
            return i
        
        if type(lst) == np.ndarray:
            sit_map[i][pos] = "X"
        else:
            sit_map[pos][i] = "X"

    return None 

# steps = 0

cur_pos = start_pos
while True:
    # print(cur_pos[0], cur_pos[1])

    # for line in sit_map:
    #     print(line)

    if sit_map[cur_pos[0]][cur_pos[1]] == "^":
        crate_pos = find_nearest_hash_to_left(np.array(sit_map)[:, cur_pos[1]], cur_pos[0], cur_pos[1])

        sit_map[cur_pos[0]][cur_pos[1]] = "X"

        if crate_pos == None:
            break

        cur_pos = (cur_pos[0] - (cur_pos[0] - crate_pos - 1), cur_pos[1])

        sit_map[cur_pos[0]][cur_pos[1]] = ">"

    elif sit_map[cur_pos[0]][cur_pos[1]] == "v":
        crate_pos = find_nearest_hash_to_right(np.array(sit_map)[:, cur_pos[1]], cur_pos[0], cur_pos[1])

        sit_map[cur_pos[0]][cur_pos[1]] = "X"

        if crate_pos == None:
            break

        cur_pos = (cur_pos[0] + (crate_pos - cur_pos[0] - 1),  cur_pos[1])

        sit_map[cur_pos[0]][cur_pos[1]] = "<"

    elif sit_map[cur_pos[0]][cur_pos[1]] == ">":
        crate_pos = find_nearest_hash_to_right(sit_map[cur_pos[0]], cur_pos[1], cur_pos[0])

        sit_map[cur_pos[0]][cur_pos[1]] = "X"

        if crate_pos == None:
            break

        cur_pos = (cur_pos[0],  cur_pos[1] + (crate_pos - cur_pos[1] - 1))

        sit_map[cur_pos[0]][cur_pos[1]] = "v"

        
    elif sit_map[cur_pos[0]][cur_pos[1]] == "<":
        crate_pos = find_nearest_hash_to_left(sit_map[cur_pos[0]], cur_pos[1], cur_pos[0])

        sit_map[cur_pos[0]][cur_pos[1]] = "X"

        if crate_pos == None:
            break

        cur_pos = (cur_pos[0], cur_pos[1] - (cur_pos[1] - crate_pos - 1))

        sit_map[cur_pos[0]][cur_pos[1]] = "^"

        
print(sum(row.count("X") for row in sit_map))