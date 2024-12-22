from heapq import heappush, heappop

from dataclasses import dataclass

from typing import Self

from collections import defaultdict

from itertools import product

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

    def distance(self, other: Self):
        return abs((other - self).i) + abs((other - self).j)

    def inbound(self, n: int, m: int):
        return 0 <= self.i < n and 0 <= self.j < m

    def neighbors(self):
        for d in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + d

    def neighbors_move(self):
        for d, m in ((Pos(0, 1), ">"), (Pos(0, -1), "<"), (Pos(1, 0), "v"), (Pos(-1, 0), "^")):
            yield self + d, m

numeric_keypad = {
    Pos(0, 0): "7",
    Pos(0, 1): "8",
    Pos(0, 2): "9",
    Pos(1, 0): "4",
    Pos(1, 1): "5",
    Pos(1, 2): "6",
    Pos(2, 0): "1",
    Pos(2, 1): "2",
    Pos(2, 2): "3",
    Pos(3, 1): "0",
    Pos(3, 2): "A",
}

inv_numeric_keypad = {v: k for k, v in numeric_keypad.items()}

directional_keypad = {
    Pos(0, 1): "^",
    Pos(0, 2): "A",
    Pos(1, 0): "<",
    Pos(1, 1): "v",
    Pos(1, 2): ">",
}

inv_directional_keypad = {v: k for k, v in directional_keypad.items()}


def dijkstra(start, end, keypad):
    pqueue = [(0, start)]
    costs = {start: 0}
    path = defaultdict(list)
    # moves = ""

    while pqueue:
        curr_pos = heappop(pqueue)[1]
        
    
        if curr_pos == end:
            break
        for next, move in curr_pos.neighbors_move():
            if next not in keypad:
                continue

            new_cost = costs[curr_pos] + 1
    
            if next not in costs or new_cost <= costs[next]:
                costs[next] = new_cost
                priority = new_cost
                path[next].append((curr_pos, move))
                # moves += move
                heappush(pqueue, (priority, next))

    return path, costs[end]

def traverse_path(current, path, moves):
    if current in path:
        if len(path[current]) == 1:
            return traverse_path(path[current][0][0], path, path[current][0][1] + moves)
        
        return [traverse_path(pc[0], path, pc[1] + moves) for pc in path[current]]

    return moves + "A"


def get_moves(start, keypad, inv_keypad, code):
    current_pos = start
    moves = [""]

    for c in code:
        paths, _ = dijkstra(current_pos, inv_keypad[c], keypad)
        print(paths)

        print(c)
        current = inv_keypad[c]

        print(traverse_path(current, paths, ""))

        moves = list(map(lambda x: "".join(x), list(product(moves, traverse_path(current, paths, "")))))
 

    return moves

codes = []

with open("input.txt", "r") as file:
    for line in file:
        codes.append(line.strip())

print(codes)

for code in codes:
    print()
    print(code)

    first_moves_per_code = get_moves(Pos(3,2), numeric_keypad, inv_numeric_keypad, code)
    print(first_moves_per_code)
    exit()

    second_moves_per_code = get_moves(Pos(0,2), directional_keypad, inv_directional_keypad, first_moves_per_code)
    third_moves_per_code = get_moves(Pos(0,2), directional_keypad, inv_directional_keypad, second_moves_per_code)

    print(third_moves_per_code, len(third_moves_per_code))
    print(second_moves_per_code)
    print(first_moves_per_code)
