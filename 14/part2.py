from dataclasses import dataclass

from typing import Self
from PIL import Image

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

def print_image(rs, n, m, sec):
    image = []
    for i in range(m):
        image.append([0]*n)

    for robot in rs:
        image[robot[0].j][robot[0].i] = 255

    im = Image.fromarray(np.array(image, dtype=np.uint8))
    im.save(f"imgs/img_{sec}.png")

with open("input.txt", "r") as file:
    for line in file:
        parts = line.split()
        p_values = Pos(*tuple(map(int, parts[0].split("=")[1].split(","))))
        v_values = Pos(*tuple(map(int, parts[1].split("=")[1].split(","))))
        robots.append((p_values,v_values))

n, m = 101, 103
n_seconds = 10000

cur_robots = robots
for i in range(n_seconds):
    new_robots = []
    for robot in cur_robots:
        new_robots.append(((robot[0]+robot[1]) % Pos(n,m), robot[1]))
    
    print(i, len(new_robots))
    print_image(cur_robots, n, m, i)

    cur_robots = new_robots

# img with lowest size is probably the solution
# ls -al imgs/ -S


