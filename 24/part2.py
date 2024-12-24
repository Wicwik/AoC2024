from itertools import combinations
from copy import deepcopy

variables = {}
connections = {}

operands = {"XOR": lambda x,y: x^y, "OR": lambda x,y: x or y, "AND": lambda x,y: x and y}

with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            break

        key, value = line.strip().split(": ")
        variables[key] = bool(int(value))


    for line in file:
        values, key  = line.strip().split(" -> ")

        connections[key] = tuple(values.split(" "))

connections = dict(reversed(sorted(connections.items())))
inv_connections = {v: k for k, v in connections.items()}

def compute(connection):
    global variables
    global connections
    global operands

    # print(connection)

    if connection[0] not in variables:
        variables[connection[0]] = compute(connections[connection[0]])

    if connection[2] not in variables:
        variables[connection[2]] = compute(connections[connection[2]])

    # print(connection, variables[connection[0]], variables[connection[2]])

    return operands[connection[1]](variables[connection[0]], variables[connection[2]])

def swap_wires(x, y):
    global connections
    global inv_connections

    pom = connections[x]
    connections[x] = connections[y]
    connections[y] = pom

    inv_connections = {v: k for k, v in connections.items()}


def get_gate(x, o, y):
    global inv_connections

    if (x, o, y) in inv_connections:
        return inv_connections[(x, o, y)]
    
    if (y, o, x) in inv_connections:
        return inv_connections[(y, o, x)]

swaps = []
ccin = None
bit = 0
while True:
    x, y, z = f"x{bit:02d}", f"y{bit:02d}", f"z{bit:02d}"

    if bit == 0:
        ccin = get_gate(x, "AND", y)
    else:
        ab_xor = get_gate(x, "XOR", y) 
        ab_and = get_gate(x, "AND", y)

        cin_ab_xor = get_gate(ab_xor, "XOR", ccin)
        if cin_ab_xor is None:
            swaps += [ab_xor, ab_and]
            swap_wires(ab_xor, ab_and)
            bit = 0
            continue

        if cin_ab_xor != z:
            swaps += [cin_ab_xor, z]
            swap_wires(cin_ab_xor, z)
            bit = 0
            continue

        cin_ab_and = get_gate(ab_xor, "AND", ccin)

        cin = get_gate(ab_and, "OR", cin_ab_and)
        ccin = cin

    bit += 1
    if bit >= 44:
        break
        

for c in connections:
    variables[c] = compute(connections[c])   

xn = ""
yn = ""
result = ""
for k, v in dict(sorted(variables.items())).items():
    # print(v)

    if k[0] == "x":
        xn = str(int(v)) + xn

    if k[0] == "y":
        yn = str(int(v)) + yn

    if k[0] == "z":
        result = str(int(v)) + result

xn, yn, result = int(xn, 2), int(yn, 2), int(result, 2)

print(xn + yn, result)
print(",".join(sorted(swaps)))