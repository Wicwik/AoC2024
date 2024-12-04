xmas = "XMAS"
directions = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (1,1), (1,-1), (-1,1)]

word_search = []

def check_xmas(word_search, pos):
    xmas_count = 0

    for d in directions:
        cur_pos = pos
        for c in xmas:
            if cur_pos[0] < 0 or cur_pos[0] >= len(word_search[0]):
                break

            if cur_pos[1] < 0 or cur_pos[1] >= len(word_search):
                break

            # print(word_search[cur_pos[1]][cur_pos[0]])

            if word_search[cur_pos[1]][cur_pos[0]] == c:
                # print(c, cur_pos[1], cur_pos[0])
                cur_pos = (cur_pos[0] + d[1], cur_pos[1] + d[0])
            else:
                break
        else:
            xmas_count += 1
        
    return xmas_count

with open("input.txt", "r") as file:
    for line in file:
        word_search.append(line.strip())

print(word_search)

count = 0
for y in range(len(word_search)):
    for x in range(len(word_search[y])):
        cur_pos = (x, y)

        if word_search[cur_pos[1]][cur_pos[0]]  == "X":
            count += check_xmas(word_search, cur_pos)

print(count)
