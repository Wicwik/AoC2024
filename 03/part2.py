import re

def get_instructions(input_string):
    pattern = r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'

    instructions = re.findall(pattern, input_string)

    return instructions

sum_all = 0
do = True

with open("input.txt", "r") as file:
    for mem in file:
        instructions = get_instructions(mem)
        
        for i in instructions:
            print(i[0])

            if i[0] == "don't()":
                do = False
            
            if i[0] == "do()":
                do = True
                continue

            if do:
                sum_all += int(i[1])*int(i[2])
        

print(sum_all)