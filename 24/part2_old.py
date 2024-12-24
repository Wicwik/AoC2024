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

def swap_results(x, y):
    pom = connections[x]
    connections[x] = connections[y]
    connections[y] = pom 
    
    # print(x, y)

    del variables[x]
    del variables[y]


connections = dict(reversed(sorted(connections.items())))
combinations8 = combinations(connections.keys(), 8)

print(len(connections))

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

# print(xn, yn)
xn, yn, result = int(xn, 2), int(yn, 2), int(result, 2)

print(connections)
print(xn, yn, result)
print(xn + yn)

orig_connections = deepcopy(connections)
orig_variables = deepcopy(variables)

ii = 0
for c in combinations8:
    connections = deepcopy(orig_connections)
    variables = deepcopy(orig_variables)

    # print(c)
    for i in range(0,len(c),2):
        swap_results(c[i],c[i+1])

    for cc in c:
        # print(cc)
        try:
            variables[cc] = compute(connections[cc])
        except RecursionError:
            continue

    result = ""
    for k, v in dict(sorted(variables.items())).items():
        # print(v)

        if k[0] == "z":
            result = str(int(v)) + result

    # print(xn, yn)
    result = int(result, 2)

    if result == xn + yn:
        print(c)
        break
    else:
        print(ii, result)

    ii += 1