reg_A = 0
reg_B = 0
reg_C = 0
inst_pointer = 0
program = []
jumped = False

with open("input.txt", "r") as file:
    reg_A = int(file.readline().strip().split()[-1])
    reg_B = int(file.readline().strip().split()[-1])
    reg_C = int(file.readline().strip().split()[-1])
    file.readline()
    program = list(map(int,file.readline().strip().split()[-1].split(",")))

def combo(operand):
    global reg_A
    global reg_B
    global reg_C

    if operand <= 3:
        return operand
    elif operand < 7:
        return {4: reg_A, 5: reg_B, 6: reg_C}[operand]
    else:
        raise ValueError(f"Invalid operand {operand}")

def adv(operand):
    global reg_A

    # print(combo(operand))
    reg_A = int(reg_A/(pow(2, combo(operand))))

def bxl(operand):
    global reg_B

    reg_B = reg_B ^ operand

def bst(operand):
    global reg_B

    reg_B = combo(operand) % 8

def jnz(operand):
    global inst_pointer
    global jumped

    if reg_A != 0:
        inst_pointer = operand
        jumped = True

def bxc(operand):
    global reg_B
    global reg_C

    reg_B = reg_B ^ reg_C

def out(operand):
    return combo(operand) % 8

def bdv(operand):
    global reg_B

    reg_B = int(reg_A/(pow(2, combo(operand))))

def cdv(operand):
    global reg_C

    reg_C = int(reg_A/(pow(2, combo(operand))))

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


out_values = []

while inst_pointer < len(program):
    instruction = program[inst_pointer]
    operand = program[inst_pointer+1]
    out_value = opcodes[instruction](operand)

    # print(instruction)
    # print(reg_A)

    if out_value != None:
        out_values.append(out_value)
        

    if jumped:
        jumped = False
    else:
        inst_pointer += 2



print(",".join(map(str,out_values)))
