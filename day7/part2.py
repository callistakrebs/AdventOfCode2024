from itertools import product

def add(left, right):
    return int(left) + int(right)

def mul(left, right):
    return int(left) * int(right)

def concat(left, right):
    return int(str(left)+str(right))

equations = []
with open("day7.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        soln, nums = line.split(":")
        nums = nums.strip().split(" ")
        equations.append((soln,nums))

trues = set() 
for equation in equations:
    soln, nums = equation
    n = len(nums)

    possible_operations = product([add,mul, concat], repeat=n-1)

    for combos in possible_operations:
        curr_total = nums[0]
        i = 1
        for op in combos:
            curr_total = op(curr_total,nums[i])
            i += 1

        if curr_total == int(soln):
            trues.add(int(soln))

print(sum(trues))
