from collections import defaultdict

computers = defaultdict(list)

with open("input.txt", "r") as file:
    for line in file:
        a,b = line.strip().split("-")

        computers[a].append(b)
        computers[b].append(a)


# print(computers)

tripples = []

for comp, conn in computers.items():
    for c in conn:
        for cc in conn:
            if c != cc:
                if cc in computers[c]:
                    if not ("t" == comp[0] or "t" == c[0] or "t" == cc[0]):
                        continue

                    tripple = set([comp, c, cc])
                    if tripple not in tripples:
                        tripples.append(tripple)

print(len(tripples))
