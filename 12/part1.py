from dataclasses import dataclass

from typing import Self

garden_map = []

with open("input.txt", "r") as file:
    for line in file:
        garden_map.append(list(line.strip()))


@dataclass(frozen=True)
class Pos:
    i: int
    j: int

    def __add__(self, other: Self):
        return Pos(self.i + other.i, self.j + other.j)
    
    def __sub__(self, other: Self):
        return Pos(self.i - other.i, self.j - other.j)

    def __eq__(self, other: Self):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)

    def __hash__(self: Self):
        return hash((self.i, self.j))
    
    def __lt__(self, other: Self):
        return (self.i, self.j) < (other.i, other.j)
    
    def inbound(self, n: int, m: int):
        return 0 <= self.i < n and 0 <= self.j < m
    
    def neighbors(self):
        for d in (Pos(0,1), Pos(0,-1), Pos(1,0), Pos(-1,0)):
            yield self + d


def dfs(start : Pos, garden_map : list[list[str]]):
    queue = [start]
    region = {start}
    plant = garden_map[start.i][start.j]
    # print(plant)

    while queue:
        plot = queue.pop()

        for neigh in plot.neighbors():
            if neigh.inbound(len(garden_map), len(garden_map[0])) and neigh not in region and garden_map[neigh.i][neigh.j] == plant:
                region.add(neigh)
                queue.append(neigh)

    return region


def perimeter(region: set[Pos]):
    per = 0
    
    for plot in region:
        per += 4 - len(set(plot.neighbors()) & region)

    return per


plots = {Pos(i,j) for i in range(len(garden_map)) for j in range(len(garden_map[0]))}


price = 0

while plots:
    start = plots.pop()
    region = dfs(start, garden_map)

    area = len(region)
    per = perimeter(region)

    price += area*per

    plots -= region

print(price)