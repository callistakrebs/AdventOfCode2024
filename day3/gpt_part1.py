import re

# Open the file using a context manager and read its content
with open("day3.txt", "r") as file:
    instructions = file.read()

# Use a more descriptive variable name for the matches
pattern = r"mul\((\d{1,3}),(\d{1,3})\)" # Capturing group around (\d{1,3})'s means the MATCH will only be on that group, and strips away the rest of the string
matches = re.findall(pattern, instructions)

# Calculate the sum in a more Pythonic way using a generator expression
total_sum = sum(int(a) * int(b) for a, b in matches)

# Print the result
print(total_sum)
