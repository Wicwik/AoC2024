import numpy as np

machines = []

a = [[],[]]
b = []
with open("input.txt", "r") as file:
    for line in file:
        if "Button" in line.strip():
            x, y = line.split(":")[1].split(",")
            a[0].append(int(x.replace("X+", "").strip()))
            a[1].append(int(y.replace("Y+", "").strip()))
        
        if "Prize" in line.strip():
            x, y = line.split(":")[1].split(",")
            b.append(int(x.replace("X=", "").strip()))
            b.append(int(y.replace("Y=", "").strip()))

            machines.append((a, b))
            a = [[],[]]
            b = []
            
cost = 0

for m in machines:
    na, nb = np.round(np.linalg.solve(m[0], m[1]), 3)

    if na.is_integer() and nb.is_integer():
        cost += na*3 + nb*1

print(int(cost))