hikemap = []
start_points = []

def get_valid_steps(point, hikemap):
    value = hikemap[point[0]][point[1]]
    valid_steps = []
    
    # up
    if (point[0] - 1 >= 0) and (hikemap[point[0] - 1][point[1]] - value == 1):
        valid_steps.append((point[0] - 1, point[1]))
    # down
    if (point[0] + 1 < len(hikemap)) and (hikemap[point[0] + 1][point[1]] - value == 1):
        valid_steps.append((point[0] + 1, point[1]))
    # left
    if (point[1] - 1 >= 0) and (hikemap[point[0]][point[1] - 1] - value == 1):
        valid_steps.append((point[0], point[1] - 1))
    # down
    if (point[1] + 1 < len(hikemap[0])) and (hikemap[point[0]][point[1] + 1] - value == 1):
        valid_steps.append((point[0], point[1] + 1))

    return valid_steps

def follow_path(start_point, hikemap, visited):
    trailhead_score = 0

    next_steps = get_valid_steps(start_point, hikemap)
    
    for step in next_steps:
        trailhead_score += follow_path(step, hikemap, visited)

        if hikemap[step[0]][step[1]] == 9 and (step[0], step[1]) not in visited:
            trailhead_score += 1
            visited.append((step[0], step[1]) )

    return trailhead_score
        

with open("input.txt", "r") as file:
    for line in file:
        hikemap.append(list(map(int, line.strip())))

for i, row in enumerate(hikemap):
    for j, e in enumerate(row):
        if e == 0:
            start_points.append((i, j))

score_sum = 0

for sp in start_points:
    score_sum += follow_path(sp, hikemap, [])

print(score_sum)
