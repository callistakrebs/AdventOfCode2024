import math

with open("day9.txt") as f:
    data = list(map(int, f.read()))

i = 0
j = len(data) - 1

i_file_id = 0
j_file_id = math.ceil(len(data) / 2) - 1

new_data = []
while i <= j:
    # Make a space for the data block for the file at i
    for k in range(data[i]):
        new_data.append(i_file_id)
        data[i] -= 1
    
    # Fill the neighboring empty space with the files at the end
    max_blocks_to_move = min(data[i+1], data[j]) # min of free space and size of current end file
    for k in range(data[i+1]):
        if data[j] > 0:
            new_data.append(j_file_id)
            data[j] -= 1
        
        if data[j] == 0:
            j -= 2
            j_file_id -= 1

    i += 2
    i_file_id += 1

checksum = sum(idx * value for idx, value in enumerate(new_data))
print(checksum)