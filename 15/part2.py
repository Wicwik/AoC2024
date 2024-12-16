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
box_parts = {}
w2map = []

instructions = ""

with open("input.txt", "r") as file:
    for y, line in enumerate(file):

        wline = ""
        for x, c in enumerate(line.strip()):
            if c == "#":
                wline += "##"

            if c == "O":
                wline += "[]"

            if c == "@":
                wline += "@."
                    
            if c == ".":
                wline += ".."

        if wline != "":
            w2map.append(wline)

        if line == "\n":
            break

    for line in file:
        instructions += line.strip()


for y, line in enumerate(w2map):
    for x, c in enumerate(line.strip()):
        if c == "#":
            walls.add(Pos(x, y))

        if c == "[" or c == "]":
            box_parts[Pos(x, y)] = c
            boxes.add(Pos(x, y))

        if c == "@":
            start_pos = Pos(x, y)


for line in w2map:
    print(line)

def check_boxes(box_pos: Pos, move: Pos, boxes_to_move: set):
    if box_pos in boxes:
        if box_parts[box_pos] == "[":
            boxes_to_move.add(box_pos)
            boxes_to_move.add(box_pos + Pos(1, 0))

            wall_left, left_set  = check_boxes(box_pos + move, move, boxes_to_move)
            wall_right, right_set = check_boxes(box_pos + Pos(1, 0) + move, move, boxes_to_move)

            return wall_left and wall_right, right_set | left_set
        
        elif box_parts[box_pos] == "]":
            boxes_to_move.add(box_pos)
            boxes_to_move.add(box_pos + Pos(-1, 0))

            wall_right, right_set = check_boxes(box_pos + move, move, boxes_to_move)
            wall_left, left_set = check_boxes(box_pos + Pos(-1, 0) + move, move, boxes_to_move)

            return wall_left and wall_right, right_set | left_set
        
    elif box_pos in walls:

        return False, boxes_to_move
        
    return True, boxes_to_move

curr_pos = start_pos
for inst in instructions:
    next_pos = curr_pos + moves[inst]
    if next_pos in walls:
        continue

    if next_pos in boxes and (inst == "<" or inst == ">"):
        boxes_to_move = set()

        box_pos = next_pos
    
        while box_pos in boxes:
            boxes_to_move.add(box_pos)
            box_pos += moves[inst]

        if box_pos in walls:
            continue

        boxes -= boxes_to_move

        new_box_parts = {}
        for box in boxes_to_move:
            part = box_parts[box]
            del box_parts[box]

            boxes.add(box + moves[inst])
            new_box_parts[box + moves[inst]] = part

        for nbp in new_box_parts:
            box_parts[nbp] = new_box_parts[nbp]

    if next_pos in boxes and (inst == "v" or inst == "^"):
        box_pos = next_pos
    
        is_wall, boxes_to_move = check_boxes(box_pos, moves[inst], set())

        if not is_wall:
            continue

        boxes -= boxes_to_move

        new_box_parts = {}
        for box in boxes_to_move:
            part = box_parts[box]
            del box_parts[box]
            
            boxes.add(box + moves[inst])
            new_box_parts[box + moves[inst]] = part

        for nbp in new_box_parts:
            box_parts[nbp] = new_box_parts[nbp]

    curr_pos = next_pos

for y in range(len(w2map)):
    line = ""
    for x in range(len(w2map[0])):
        if Pos(x,y) in boxes:
            line += box_parts[Pos(x,y)]

        elif Pos(x,y) in walls:
            line += "#"

        elif Pos(x,y) == curr_pos:
            line += "@"

        else:
            line += "."

    print(line)

sumboxes = 0
for box in boxes:
    if box_parts[box] == "[":
        sumboxes += box.j*100 + box.i

print(sumboxes)
        