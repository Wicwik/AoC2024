from collections import defaultdict
from itertools import permutations

antennas = defaultdict(list)

def vector(a, b):
    return (b[0] - a[0], b[1] - a[1])

def move(a, b):
    return (a[0] + b[0], a[1] + b[1])

def neg(a):
    return (-a[0], -a[1])

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        for j, a in enumerate(line.strip()):
            if a != ".":
                antennas[a].append((i,j))

antmap_max = (i, j)
# print(antmap_max)

ant_perms = defaultdict(list)
for a in antennas:
    for comb in permutations(antennas[a], 2):
            ant_perms[a].append(comb)

# print(ant_perms)

antinodes = set()
for a in ant_perms:
    if len(ant_perms[a]) > 1:
        for ap in ant_perms[a]:
            v = vector(ap[0], ap[1])
            antinode = move(ap[1], v)

            if (antinode[0] <= antmap_max[0] and antinode[0] >= 0) and (antinode[1] <= antmap_max[1] and antinode[1] >= 0) :
                antinodes.add(antinode)
# print(antinodes)
print(len(antinodes))
