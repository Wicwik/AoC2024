from collections import defaultdict

computers = defaultdict(list)

with open("input.txt", "r") as file:
    for line in file:
        a,b = line.strip().split("-")

        computers[a].append(b)
        computers[b].append(a)


# print(computers)

comp_sets = []

for comp, conn in computers.items():
    s = set()
    s.add(comp)
    comp_sets.append(s)

    for comp_set in comp_sets:
        if all([c in computers[comp] for c in comp_set]):
            comp_set.add(comp)


print(",".join(sorted(list(max(comp_sets, key=len)))))




