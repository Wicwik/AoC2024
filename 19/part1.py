from typing import List

towels : List[str] = []
designs : List[str] = []

with open("input.txt", "r") as file:
    towels = file.readline().strip().split(", ")
    file.readline()

    for line in file:
        designs.append(line.strip())

cache = {}
def is_possible(design : str, towels : List[str]):
    if design in cache:
          return cache[design]

    if design == "":
        return True

    matches = []
    for towel in towels:
        if design.startswith(towel):
            matches.append(towel)

    for m in matches:
        if is_possible(design[len(m):], towels):
            cache[design] = True
            return True
    
    cache[design] = False
    return False

print(sum([is_possible(design, towels) for design in designs]))