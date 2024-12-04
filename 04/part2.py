# patterns ftw

word_search = []

with open("input.txt", "r") as file:
    for line in file:
        word_search.append(line.strip())

def check_xmas(word_search, pos):
    cond = (
        word_search[pos[1] - 1][pos[0] - 1] == "M"
        and word_search[pos[1] - 1][pos[0] + 1] == "M"
        and word_search[pos[1] + 1][pos[0] + 1] == "S"
        and word_search[pos[1] + 1][pos[0] - 1] == "S"
    )

    if cond: 
        return 1

    cond = (
        word_search[pos[1] - 1][pos[0] - 1] == "S"
        and word_search[pos[1] - 1][pos[0] + 1] == "S"
        and word_search[pos[1] + 1][pos[0] + 1] == "M"
        and word_search[pos[1] + 1][pos[0] - 1] == "M"
    )

    if cond: 
        return 1

    cond = (
        word_search[pos[1] - 1][pos[0] - 1] == "M"
        and word_search[pos[1] - 1][pos[0] + 1] == "S"
        and word_search[pos[1] + 1][pos[0] + 1] == "S"
        and word_search[pos[1] + 1][pos[0] - 1] == "M"
    )

    if cond: 
        return 1

    cond = (
        word_search[pos[1] - 1][pos[0] - 1] == "S"
        and word_search[pos[1] - 1][pos[0] + 1] == "M"
        and word_search[pos[1] + 1][pos[0] + 1] == "M"
        and word_search[pos[1] + 1][pos[0] - 1] == "S"
    )

    if cond: 
        return 1
    
    return 0

count = 0

for y in range(1, len(word_search) -1):
    for x in range(1, len(word_search[y])-1):
        cur_pos = (x, y)

        if word_search[cur_pos[1]][cur_pos[0]]  == "A":
            count += check_xmas(word_search, cur_pos)

print(count)
