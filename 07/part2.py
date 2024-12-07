import numpy as np
from itertools import product

def apply_operator(a, b, op):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b
    elif op == "||":
        return int(str(a) + str(b))
    else:
        raise ValueError(f"Unsupported operator: {op}")


calculations = {}

with open("input.txt", "r") as file:
    for line in file:
        calculations[int(line.strip().split(":")[0])] = np.array(list(map(int, line.strip().split(":")[1].strip().split(" "))))

print(calculations)

tot_cal_res = 0

operators = ["*", "+", "||"]

for c, e in calculations.items():
    combinations = list(product(operators, repeat=len(e) - 1))

    for comb in combinations:
        intermediate = e[0]
        for i, op in enumerate(comb):
            intermediate = apply_operator(intermediate, e[i+1], op)
    
        if intermediate == c:
            tot_cal_res += c
            break


print(tot_cal_res)