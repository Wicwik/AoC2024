
import numpy as np

reports = []

with open("input.txt", "r") as file:
    for line in file:
        if line.strip():
            reports.append(list(map(int,line.split())))

safe = 0


def is_safe(report):
    diff = np.diff(np.array(report))

    return (np.all(diff > 0) or np.all(diff < 0)) and (np.all(np.abs(diff) <= 3))


for report in reports:
    if any(is_safe(report[:i] + report[i+1:]) for i in range(len(report))):
        safe += 1
    

print(safe)
