
import numpy as np

reports = []

with open("input.txt", "r") as file:
    for line in file:
        if line.strip():
            reports.append(list(map(int,line.split())))

safe = 0

for report in reports:
    diff = np.diff(np.array(report))
    if (np.all(diff > 0) or np.all(diff < 0)) and (np.all(np.abs(diff) <= 3)):
        safe += 1

print(safe)