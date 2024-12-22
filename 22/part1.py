secret_numbers = []

with open("input.txt", "r") as file:
    for line in file:
        secret_numbers.append(int(line.strip()))

def get_next_secret_number(secret_number):
    step_one = (secret_number^(secret_number * 64)) % 16777216
    step_two = (step_one^(step_one//32)) % 16777216
    step_three = (step_two^(step_two*2048)) % 16777216
    
    return step_three

def get_nth_secret_number(secret_number, n):
    nth_secret_number = secret_number
    for _ in range(n):
        nth_secret_number = get_next_secret_number(nth_secret_number)


    return nth_secret_number

sum_secret_numbers = 0
for secret_number in secret_numbers:
    sum_secret_numbers += get_nth_secret_number(secret_number, 2000)

print(sum_secret_numbers)