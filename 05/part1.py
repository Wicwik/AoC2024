from collections import defaultdict

rules = defaultdict(set)
orderings = []


with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            break

        rule = line.strip().split("|")
        rules[int(rule[0])].add(int(rule[1]))

    for line in file:
        orderings.append([int(i) for i in line.strip().split(",")])


correct = []

for ordering in orderings:
    for i in range(1, len(ordering)):
        # print(ordering[i-1], rules[ordering[i]], ordering[i])
        if ordering[i-1] in rules[ordering[i]]:
            break
    else:
        correct.append(ordering)
    
middle_sum = 0

for c in correct:
    n = len(c)

    middle_sum += c[n//2]

print(middle_sum)
