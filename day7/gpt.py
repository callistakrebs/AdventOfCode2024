def add(left, right):
    return left + right

def mul(left, right):
    return left * right

def concat(left, right):
    return int(str(left) + str(right))

def can_solve(nums, target, index=1, current=None):
    # Initialize the `current` total with the first number
    if current is None:
        current = nums[0]

    # Base case: If we've processed all numbers, check the result
    if index == len(nums):
        return current == target

    # Try all operations with the current number and the next number
    for operation in (add, mul, concat):
        next_value = operation(current, nums[index])
        if can_solve(nums, target, index + 1, next_value):
            return True

    # If no operation leads to the target, return False
    return False

# Read and process input
equations = []
with open("day7.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        soln, nums = line.split(":")
        nums = list(map(int, nums.strip().split(" ")))
        equations.append((int(soln), nums))

# Find valid solutions
trues = set()
for soln, nums in equations:
    if can_solve(nums, soln):
        trues.add(soln)

# Print the sum of valid solutions
print(sum(trues))
