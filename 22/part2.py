from itertools import pairwise
from collections import defaultdict

secret_numbers = []

with open("input.txt", "r") as file:
    for line in file:
        secret_numbers.append(int(line.strip()))

def get_next_secret_number(secret_number):
    step_one = (secret_number^(secret_number * 64)) % 16777216
    step_two = (step_one^(step_one//32)) % 16777216
    step_three = (step_two^(step_two*2048)) % 16777216
    
    return step_three

bananas = defaultdict(int)
numbers = []
for secret_number in secret_numbers:
    numbers = [secret_number] + [secret_number:= get_next_secret_number(secret_number) for _ in range(2000)]
    diffs = [b%10 - a%10 for a,b in pairwise(numbers)]

    visited = set()
    for i in range(len(diffs)-3):
        pattern = tuple(diffs[i:i+4])
        if pattern not in visited:
            bananas[pattern] += numbers[i+4] % 10 
            visited.add(pattern)


print(max(bananas.values()))