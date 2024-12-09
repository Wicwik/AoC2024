with open("input.txt", "r") as file:
    disk_map = file.readline().strip()

def find_suitable_empty_block(empty_blocks, file_block):
    for i ,eb in enumerate(empty_blocks):
        if file_block[1] <= eb[1] and eb[0] < file_block[0]:
            return i, eb
    
    return None,None

block_map = []
empty_blocks = []
file_blocks = []

block_count = 0
for i, b in enumerate(disk_map):
    if i % 2 == 1:
        empty_blocks.append((len(block_map),int(b)))
        block_map += ["."]*int(b)
    else:
        file_blocks.append((len(block_map),int(b)))
        block_map += [str(block_count)]*int(b)
        block_count += 1


for i, fb in reversed(list(enumerate(file_blocks))):
    seb_i, seb = find_suitable_empty_block(empty_blocks, fb)
    
    if seb:
        if seb[1] > fb[1]:
            block_map[seb[0]:seb[0]+seb[1]] = block_map[fb[0]:fb[0]+fb[1]] + ["."]*(seb[1]-fb[1])
            block_map[fb[0]:fb[0]+fb[1]] = ["."]*fb[1]
            empty_blocks[seb_i] = ((seb[0]+fb[1], seb[1]-fb[1]))
        else:
            block_map[seb[0]:seb[0]+seb[1]] = block_map[fb[0]:fb[0]+fb[1]]
            block_map[fb[0]:fb[0]+fb[1]] = ["."]*fb[1]
            empty_blocks.pop(seb_i)

checksum = 0

for i, b in enumerate(block_map):
    if b != ".":
        checksum += i*int(b)

print(checksum)