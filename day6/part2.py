import copy

with open("day6.txt") as f:
    map = f.read().split("\n")
    map = [list(row) for row in map]

    route = copy.deepcopy(map)
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                start = (i,j)
                # route[i][j] = "X"

    i, j = start
    curr_direction = "up"

    count = 0
    for k in range(len(map)):
        for m in range(len(map[k])):
            route = copy.deepcopy(map)
            i, j = start
            curr_direction = "up"
            loop = False
            barriers_found = {}
            while i < len(map) and j < len(map[i]) and i >= 0 and j >= 0 and not loop:
                if (i,j) in barriers_found and barriers_found[(i,j)] == curr_direction:
                    # we are at a barrier we have hit before
                    loop = True
                    count += 1
                
                else:
                    if map[i][j] == "#" or (i,j) == (k,m):
                        barriers_found[(i,j)] = curr_direction
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
                        if curr_direction == "left" or curr_direction == "right":
                            if route[i][j] == ".":
                                route[i][j] = "-"
                                
                            if route[i][j] == "|":
                                route[i][j] = "+"

                        if curr_direction == "up" or curr_direction == "down":
                            if route[i][j] == ".":
                                route[i][j] = "|"

                            if route[i][j] == "-":
                                route[i][j] = "+"


                    if curr_direction == "up":
                        i -= 1
                    if curr_direction == "down":
                        i += 1
                    if curr_direction == "left":
                        j -= 1
                    if curr_direction == "right":
                        j += 1

print(count)