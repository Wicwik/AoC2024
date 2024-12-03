import re


def get_muls(input_string):
    pattern = r'mul\((\d+),(\d+)\)'

    matches = re.findall(pattern, input_string)

    numbers = [int(match[0])*int(match[1]) for match in matches]

    return numbers

sum_all = 0

with open("input.txt", "r") as file:
    for mem in file:
        sum_all += sum(get_muls(mem))

print(sum_all)