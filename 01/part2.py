list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        if line.strip():
            values = line.split()
            if len(values) == 2:
                list1.append(int(values[0]))
                list2.append(int(values[1]))

sim_score = 0

for i in list1:
    sim_score += i*list2.count(i)

print(sim_score)