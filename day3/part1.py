import re

with open("day3.txt") as f:
    instructions = f.read()
    multipliers = re.findall("mul\\(\\d\\d?\\d?,\\d\\d?\\d?\\)", instructions)
    
    sum = 0
    for item in multipliers:
        nums = list(map(int,item.strip("mul()").split(",")))
        sum += nums[0] * nums[1]

print(sum)