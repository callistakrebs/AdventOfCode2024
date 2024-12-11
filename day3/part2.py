import re

with open("day3.txt") as f:
    instructions = f.read()
    multipliers = re.findall("mul\\(\\d\\d?\\d?,\\d\\d?\\d?\\)|do\\(\\)|don\\'t\\(\\)", instructions)
    
    sum = 0
    enabled = True
    for item in multipliers:
        if item == "do()":
            enabled = True
        
        if item == "don't()":
            enabled = False
        
        if enabled and item.startswith("mul"):
            nums = list(map(int,item.strip("mul()").split(",")))
            sum += nums[0] * nums[1]

print(sum)