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

def get_counts(code):
    new_code = ""
    counts = {}
    for c in code:
        new_code += c
        if c == "A":
            if new_code not in counts:
                counts[new_code] = 0
            counts[new_code] += 1

            new_code = ""

    return counts

def get_keypad_moves(current_pos, keypad, code):
    numeric = current_pos == Pos(3,2)
    moves = ""
    for c in code:
        old_moves = moves
        cpos = keypad[c]
        dpos = cpos - current_pos

        if dpos.j == 2 and dpos.i > 0 and cpos.i == 3 and numeric:
            moves += ">" * dpos.j + "v" * dpos.i
        elif dpos.j == -2 and dpos.i < 0 and current_pos.i == 3 and numeric:
            moves += "^" * abs(dpos.i) + "<<"
        elif dpos.j == -1 and current_pos.j == 1 and dpos.i < 0 and current_pos.i == 3 and numeric:
            moves += "^" * abs(dpos.i) + "<"
        elif not numeric and dpos.j == 2 and dpos.i == -1:
            moves += ">>^"
        elif not numeric and dpos.j == -2 and dpos.i == 1:
            moves += "v<<"
        elif not numeric and dpos.j == -1 and dpos.i == 1 and current_pos.j == 1 and current_pos.i == 0:
            moves += "v<"
        elif not numeric and dpos.j == 1 and dpos.i == -1 and current_pos.j == 0 and current_pos.i == 1:
            moves += ">^"
        else:
            if dpos.j < 0:
                moves += "<" * abs(dpos.j)
            if dpos.i < 0:
                moves += "^" * abs(dpos.i)
            else:
                moves += "v" * abs(dpos.i)
            if dpos.j > 0:
                moves += ">" * abs(dpos.j)

        
        # if len(old_moves) == len(moves):
        #     print("woops!", c)

        moves += "A"
        current_pos = cpos

    return moves

def get_moves(start, keypad, counts):
    new_moves = {}
    for code, count in counts.items():
        for c, ccount in get_counts(get_keypad_moves(start, keypad, code)).items():
            if c not in new_moves:
                new_moves[c] = 0

            new_moves[c] += ccount * count

    return new_moves

codes = []

with open("input.txt", "r") as file:
    for line in file:
        codes.append(line.strip())

print(codes)

complexity = 0
for code in codes:

    first_moves_per_code = get_moves(Pos(3,2), inv_numeric_keypad, get_counts(code))
    second_moves_per_code = get_moves(Pos(0,2), inv_directional_keypad, first_moves_per_code)
    third_moves_per_code = get_moves(Pos(0,2), inv_directional_keypad, second_moves_per_code)
    # print(third_moves_per_code)

    l = 0
    for c, count in third_moves_per_code.items():
        l += len(c) * count

    complexity += l*int(code[:3])

print(complexity)

