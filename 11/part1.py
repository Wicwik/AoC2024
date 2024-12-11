with open("input.txt", "r") as file:
    init_stones = file.readline().strip().split()

n_blinks = 25

print(init_stones)

stones = init_stones
for _ in range(n_blinks):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones += ["1"]

        elif len(stone) % 2 == 0:
            # print(stone[:len(stone)//2], stone[len(stone)//2:])
            new_stones += [stone[:len(stone)//2], str(int(stone[len(stone)//2:]))]

        else:
            new_stones += [str(int(stone)*2024)]

    # print(new_stones)
    stones = new_stones

print(len(stones))