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


    if connection[0] not in variables:
        variables[connection[0]] = compute(connections[connection[0]])

    if connection[2] not in variables:
        variables[connection[2]] = compute(connections[connection[2]])

    # print(connection, variables[connection[0]], variables[connection[2]])

    return operands[connection[1]](variables[connection[0]], variables[connection[2]])


connections = dict(reversed(sorted(connections.items())))


for c in connections:
    variables[c] = compute(connections[c])   

result = ""
for k, v in dict(sorted(variables.items())).items():

    if k[0] == "z":
        result = str(int(v)) + result

print(int(result, 2))