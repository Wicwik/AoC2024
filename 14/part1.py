from dataclasses import dataclass

from typing import Self

import numpy as np

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
    
    def inbound(self, n: int, m: int):
        return 0 <= self.i < n and 0 <= self.j < m
    
    def neighbors(self):
        for d in (Pos(0,1), Pos(0,-1), Pos(1,0), Pos(-1,0)):
            yield self + d

robots = []

with open("input.txt", "r") as file:
    for line in file:
        parts = line.split()
        p_values = Pos(*tuple(map(int, parts[0].split("=")[1].split(","))))
        v_values = Pos(*tuple(map(int, parts[1].split("=")[1].split(","))))
        robots.append((p_values,v_values))

n, m = 101, 103
n_seconds = 100

cur_robots = robots
for _ in range(n_seconds):
    new_robots = []
    for robot in cur_robots:
        new_robots.append(((robot[0]+robot[1]) % Pos(n,m), robot[1]))

    cur_robots = new_robots


x_mid = n//2
y_mid = m//2

quadrons = [0,0,0,0]

for robot in cur_robots:
    if robot[0].i < x_mid and robot[0].j < y_mid:
        quadrons[0] += 1
    elif robot[0].i > x_mid and robot[0].j > y_mid:
        quadrons[3] += 1
    elif robot[0].i > x_mid and robot[0].j < y_mid:
        quadrons[1] += 1
    elif robot[0].i < x_mid and robot[0].j > y_mid:
        quadrons[2] += 1


print(np.prod(quadrons))

