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


incorrect = []

for ordering in orderings:
    i = 1
    added = False

    while i < len(ordering):
        # print(ordering[i-1], rules[ordering[i]], ordering[i])
        if ordering[i-1] in rules[ordering[i]]:
            if not added:
                incorrect.append(ordering)
                added = True

            pom = ordering[i-1]
            ordering[i-1] = ordering[i]
            ordering[i] = pom
            i = 1
        else:
            i += 1


# print(incorrect)

middle_sum = 0

for c in incorrect:
    n = len(c)

    middle_sum += c[n//2]

print(middle_sum)
