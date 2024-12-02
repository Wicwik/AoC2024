import numpy as np

list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        if line.strip():
            values = line.split()
            if len(values) == 2:
                list1.append(int(values[0]))
                list2.append(int(values[1]))

list1 = np.array(sorted(list1))
list2 = np.array(sorted(list2))

print(sum(np.abs(list2 - list1)))