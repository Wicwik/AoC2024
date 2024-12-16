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
            for prio, d, new_rot in ((1, Pos(0,1), ">"), (1001, Pos(1,0), "v"), (1001, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "<":
            for prio, d, new_rot in ((1, Pos(0,-1), "<"), (1001, Pos(1,0), "v"), (1001, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "v":
            for prio, d, new_rot in ((1001, Pos(0,1), ">"), (1001, Pos(0,-1), "<"), (1, Pos(1,0), "v")):
                yield (prev_prio + prio, self + d, new_rot, prev_path + [self + d])

        elif rotation == "^":
            for prio, d, new_rot  in ((1001, Pos(0,1), ">"), (1001, Pos(0,-1), "<"), (1, Pos(-1,0), "^")):
                yield (prev_prio + prio, self + d, new_rot , prev_path + [self + d])

    


walls = set()
maze = []
with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        maze.append(list(line.strip()))
        for j, c in enumerate(line.strip()):
            if c == "#":
                walls.add(Pos(i,j))

            if c == "E":
                end = Pos(i,j)

            if c == "S":
                start = Pos(i,j)

pqueue = []

curr_pos = start
curr_rotation = ">"

visited = {start: 0}

for n in curr_pos.neighbors_prio(curr_rotation, 0, []):
    if n[1] not in walls:
        heappush(pqueue, n)


paths = []
while pqueue:
    # print(pqueue)

    curr = heappop(pqueue)
    curr_pos = curr[1]
    curr_rotation = curr[2]
    curr_prio = curr[0]
    curr_path = curr[3]

    if curr_pos == end:
        visited[curr_pos] = curr_prio
        target_state = curr
        

    for n in curr_pos.neighbors_prio(curr_rotation, curr_prio, curr_path):
        if curr_pos == Pos(7,3):
            print(n)
        if (n[1] not in walls) and ((n[1] not in visited) or (visited[n[1]] > n[0])):
            heappush(pqueue, n)
    
    visited[curr_pos] = curr_prio

curr = target_state
print(curr[3])
print(len(curr[3]), curr[0], curr[1])
# print(curr)
# print(pqueue)
# print(len(visited))

to_visit = [curr]
print(visited[curr[1]])

seen = set()
while to_visit:
    curr = to_visit.pop(0)
    curr_pos = curr[1]
    curr_rotation = curr[2]

    seen.add(curr[1])

    for r in ("<", ">", "v", "^"):
        for n in curr_pos.neighbors_prio(r, 0, []):
            # print(n[1])
            if (n[1] not in walls) and (n[1] in visited):
                # print(visited[n[1]] + n[0], visited[curr_pos])
                if visited[n[1]] + n[0] == visited[curr_pos]:
                    # print(curr_pos, n[1])
                    to_visit.append((n[0], n[1], n[2], n[3]))

print(len(visited))
print(len(seen))
# print(visited)
# print(seen)
print(visited[Pos(7,3)], visited[Pos(7,4)], visited[Pos(7,5)], visited[Pos(8,5)], visited[Pos(7,6)])
print(seen)

for s in seen:
    maze[s.i][s.j] = "O"

for m in maze:
    print(m)