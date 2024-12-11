from collections import defaultdict

with open("input.txt", "r") as file:
    line = file.readline().strip().split()
    init_stones = dict(zip(map(int, line), len(line)*[1]))

n_blinks = 75

print(init_stones)

def update(new_stones, stone, count):
    new_stones[stone] += count


stones = init_stones
for _ in range(n_blinks):
    new_stones = defaultdict(lambda: 0)

    for stone, count in stones.items():
        if stone == 0:
            update(new_stones, 1, count)

        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            update(new_stones, int(str_stone[:len(str_stone)//2]), count)
            update(new_stones, int(str_stone[len(str_stone)//2:]), count)

        else:
            update(new_stones, stone*2024, count)

    # print(new_stones)
    stones = new_stones

print(sum(stones.values()))