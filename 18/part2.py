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
    
    def neighbors_prio(self, prev_prio):
        for d in (Pos(0,1), Pos(0,-1), Pos(1,0), Pos(-1,0)):
            yield (prev_prio + 1, self + d)

walls = []

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        pos = list(map(int,line.strip().split(",")))
        walls.append(Pos(pos[1], pos[0]))


def reachable(cutoff, all_walls, n ,m):
    start = Pos(0,0)
    end = Pos(n,m)
    walls = set(all_walls[:cutoff])

    pqueue = [(0, start)]
    costs = {start: 0}


    while pqueue:
        curr_pos = heappop(pqueue)[1]
    
        if curr_pos == end:
            return True

        for next in curr_pos.neighbors():
            if next in walls:
                continue

            if not next.inbound(n+1,m+1):
                continue

            new_cost = costs[curr_pos] + 1

            if next not in costs or new_cost < costs[next]:
                costs[next] = new_cost
                priority = new_cost
                heappush(pqueue, (priority, next))

    return False

cutoff = 1024
n, m = 70, 70

low, high = 0, len(walls)

while low != high:
    mid = (low + high) //2
    if reachable(mid, walls, n, m):
        low = mid +1
    else:
        high = mid

print(f"{walls[low-1].j},{walls[low-1].i}")