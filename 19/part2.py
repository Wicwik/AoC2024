from typing import List

towels : List[str] = []
designs : List[str] = []

with open("input.txt", "r") as file:
    towels = file.readline().strip().split(", ")
    file.readline()

    for line in file:
        designs.append(line.strip())

cache = {}
def every_possible(design : str, towels : List[str]):
    if design in cache:
          return cache[design]

    if design == "":
        return 1

    matches = []
    for towel in towels:
        if design.startswith(towel):
            matches.append(towel)

    n_ways = []
    for m in matches:
        n_ways.append(every_possible(design[len(m):], towels))
    
    cache[design] = sum(n_ways)
    return cache[design] 

print(sum([every_possible(design, towels) for design in designs]))