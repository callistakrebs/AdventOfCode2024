with open("day9.txt") as f:
    data = list(map(int, f.read()))

file_id = 0
new_data = []
file_idxs = {}
free_space_idxs = {}
for i in range(0,len(data), 2):
    file_idxs[file_id] = len(new_data)
    free_space_idxs[i+1] = len(new_data) + data[i]
    for k in range(data[i]):
        new_data.append(file_id)
    if i+1 <= len(data) - 1:
        for k in range(data[i+1]):
            new_data.append(-1)
    file_id += 1

for j in range(len(data) - 1, 0, -2):
    moved = False
    file_id = int(j / 2)
    i = 0
    old_idx = file_idxs[file_id]
    while i <= j and not moved:
        if data[i] >= data[j] and i % 2 != 0:
            moved = True
            new_idx = free_space_idxs[i]

            # move file in the new data list
            new_data[new_idx : new_idx + data[j]] = [file_id] * data[j]
            new_data[old_idx : old_idx + data[j]] = [-1] * data[j]

            # Update data free space and file space values
            data[i] = data[i] - data[j]
            data[j-1] = data[j-1] + data[j]
            free_space_idxs[i] += data[j]

        i += 1

sum = 0
for idx, val in enumerate(new_data):
    if val >= 0:
        sum += idx * val
print(sum)