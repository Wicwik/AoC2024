with open("input.txt", "r") as file:
    disk_map = file.readline().strip()

def find_last_digit(l):
    for i, e in reversed(list(enumerate(l))):
        if e.isdigit():
            return i

block_map = []
empty_blocks = []
last_block_pos = None

block_count = 0
for i, b in enumerate(disk_map):
    if i % 2 == 1:
        empty_blocks.append((len(block_map),int(b)))
        block_map += ["."]*int(b)
    else:
        last_block_pos = len(block_map)-1+int(b)
        block_map += [str(block_count)]*int(b)
        block_count += 1

for eb in empty_blocks:
    i = 0
    while i < eb[1]:
        if block_map[-1].isdigit():
            block_map[eb[0]+i] = block_map[-1]
            i += 1
            block_map.pop()
        else:
            block_map.pop()

    if "." not in block_map[:find_last_digit(block_map)+1]:
        break

checksum = 0

for i, b in enumerate(block_map[:find_last_digit(block_map)+1]):
    checksum += i*int(b)

print(checksum)