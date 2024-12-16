from heapq import heappush, heappop

from dataclasses import dataclass

from typing import Self

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
    
    def __mod__(self, other: Self):
        return Pos(self.i % other.i, self.j % other.j)
    
    def __rmul__(self, other: int):
        return Pos(self.i * other, self.j * other)
    
    def inbound(self, n: int, m: int):
        return 0 <= self.i < n and 0 <= self.j < m
    
    def neighbors(self):
        for d in (Pos(0,1), Pos(0,-1), Pos(1,0), Pos(-1,0)):
            yield self + d

    def neighbors_prio(self, rotation, prev_prio, prev_path):
        if rotation == ">":
            for prio, d, new_rot in ((1, Pos(0,1), ">"), (2001, Pos(0,-1), "<"), (1001, Pos(1,0), "v"), (1001, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "<":
            for prio, d, new_rot in ((2001, Pos(0,1), ">"), (1, Pos(0,-1), "<"), (1001, Pos(1,0), "v"), (1001, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "v":
            for prio, d, new_rot in ((1001, Pos(0,1), ">"), (1001, Pos(0,-1), "<"), (1, Pos(1,0), "v"), (2001, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "^":
            for prio, d, new_rot  in ((1001, Pos(0,1), ">"), (1001, Pos(0,-1), "<"), (2001, Pos(1,0), "v"), (1, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot , prev_path + [self + d])

    


walls = set()

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line):
            if c == "#":
                walls.add(Pos(i,j))

            if c == "E":
                end = Pos(i,j)

            if c == "S":
                start = Pos(i,j)

pqueue = []
visited = [start]

curr_pos = start
curr_rotation = ">"
for n in curr_pos.neighbors_prio(curr_rotation, 0, []):
    if n[1] not in walls:
        heappush(pqueue, n)

while pqueue:
    # print(curr_pos)

    curr = heappop(pqueue)
    curr_pos = curr[1]
    curr_rotation = curr[2]
    curr_prio = curr[0]
    curr_path = curr[3]

    if curr_pos == end:
        break

    for n in curr_pos.neighbors_prio(curr_rotation, curr_prio, curr_path):
        if (n[1] not in walls) and (n[1] not in visited):
            heappush(pqueue, n)
    
    visited.append(curr_pos)

print(curr[0])

# n_steps = 0
# curr_back = curr[1]
# while curr_back.prev:
#     n_steps += 1
#     curr_back = curr_back.prev
