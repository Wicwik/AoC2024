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

moves = {">": Pos(1,0), "<": Pos(-1,0), "v": Pos(0,1), "^": Pos(0,-1)}

walls = set()
boxes = set()
wmap = []

instructions = ""

with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add(Pos(x, y))

            if c == "O":
                boxes.add(Pos(x, y))

            if c == "@":
                start_pos = Pos(x, y)
        
        if line.strip() != "":
            wmap.append(line.strip())

        if line == "\n":
            break

    for line in file:
        instructions += line.strip()

curr_pos = start_pos
for inst in instructions:
    next_pos = curr_pos + moves[inst]
    if next_pos in walls:
        continue

    if next_pos in boxes:
        boxes_to_move = set()

        box_pos = next_pos
    
        while box_pos in boxes:
            boxes_to_move.add(box_pos)
            box_pos += moves[inst]

        if box_pos in walls:
            continue

        boxes -= boxes_to_move

        for box in boxes_to_move:
            boxes.add(box + moves[inst])

    curr_pos = next_pos

for y in range(len(wmap)):
    line = ""
    for x in range(len(wmap[0])):
        if Pos(x,y) in boxes:
            line += "O"

        elif Pos(x,y) in walls:
            line += "#"

        elif Pos(x,y) == curr_pos:
            line += "@"

        else:
            line += "."

    print(line)

sumboxes = 0
for box in boxes:
    sumboxes += box.j*100 + box.i

print(sumboxes)
        