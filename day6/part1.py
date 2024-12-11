import copy

with open("day6.txt") as f:
    map = f.read().split("\n")
    map = [list(row) for row in map]

    route = copy.deepcopy(map)
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                start = (i,j)
                route[i][j] = "X"
 
    i, j = start
    curr_direction = "up"
    count = 0
    while i < len(map) and j < len(map[i]) and i >= 0 and j >= 0:
        if map[i][j] == "#":
            if curr_direction == "up":
                i += 1
                curr_direction = "right"
            elif curr_direction == "right":
                j -= 1
                curr_direction = "down"
            elif curr_direction == "down":
                i -= 1
                curr_direction = "left"
            elif curr_direction == "left":
                j += 1
                curr_direction = "up"
        else:
            route[i][j] = "X"
        
        if curr_direction == "up":
            i -= 1
        if curr_direction == "down":
            i += 1
        if curr_direction == "left":
            j -= 1
        if curr_direction == "right":
            j += 1

count = 0 
for line in route:
    for j in range(len(route)):
        if line[j] == "X":
            count+=1

print(count)