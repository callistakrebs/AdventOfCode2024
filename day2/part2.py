def check_safe(levels):
    safe = False
    levels_copy = levels.copy()
    levels_copy.sort() # sort forwards and see if its the same
    if levels == levels_copy:
        safe = True
    
    levels_copy.sort(reverse=True) # sort backwards and see if its the same
    if levels == levels_copy:
        safe = True

    last = int(levels[0])
    i = 1
    while safe and i < len(levels):
        if abs(int(levels[i]) - last) >= 1 and abs(int(levels[i]) - last) <= 3:
            safe = True
        else:
            safe = False
        
        last = int(levels[i])
        i += 1

    return safe

with open("day2.txt") as f:
    count = 0
    for line in f.readlines():
        safe = False
        levels = [int(x) for x in line.strip().split(" ")]
        safe = check_safe(levels)
        
        if not safe:
            i = 0
            while not safe and i < len(levels):
                safe = check_safe(levels[0:i] + levels[i+1:])
                i += 1

        if safe:
            count +=1

print(count)