### My Original Code
```py
left = []
right = []
with open("day1.txt") as f:
    for line in f.readlines():
        line.replace("\n","")
        curr = line.split("   ")
        left.append(int(curr[0]))
        right.append(int(curr[1]))

left.sort()
right.sort()

right_count = {}
for i in range (len(right)):
    if right[i] in right_count.keys():
        right_count[right[i]] += 1
    else:
        right_count[right[i]] = 1 

score = 0
for i in range(len(left)):
    if left[i] in right_count.keys():
        score += left[i] * right_count[left[i]]
    else:
        score += left[i] * 0

print(score)
```
### ChatGPT's Improved Version
```py
from collections import Counter

# Initialize lists
left = []
right = []

# Read and process the file
with open("day1.txt") as f:
    for line in f:
        # Strip newline characters and split the line into parts
        curr = line.strip().split("   ")
        # Append values to respective lists
        left.append(int(curr[0]))
        right.append(int(curr[1]))

# Sort the lists (not strictly necessary for the given logic but kept if needed elsewhere)
left.sort()
right.sort()

# Use Counter to simplify counting occurrences in the 'right' list
right_count = Counter(right)

# Calculate the score
score = sum(left[i] * right_count.get(left[i], 0) for i in range(len(left)))

# Print the final score
print(score)

```
# What I Learned
### Strip()
> * Newline characters can be stripped in a one line function call Strip(). 
> * Strip() with no arguments removes leading and trailing white spaces in a string. 
> * You can also pass arguments to strip() to remove specified characters:
```
my_string = "hello there !!!!! .."
my_stripped_string = my_string.strip("!.")
print(my_stripped_string)
# Outputs "hello there "
```

### Collections.Counter
> * Collections.Counter() tallies the number of occurrences of elements in a list. The input is a list and the output is a dictionary where each element in the list is a key and the value is the number of times the element occurs in the list.
> * Counter items return 0 count for missing elements instead of raising a `KeyError` 
> * Elements can have 0 count, negative count
> * Removing a key from the counter will remove all instances of the key in the iterator generated by `counter.elements()`
> * You can also use Counter to generate lists with a certain number of elements. For example:
```
a = Counter(a=3,b=2)
sorted(a.elements())
# outputs ['a','a','a','b','b']
```

### Dict.get()
> * Can use dict.get() when retreiving elements from a hashset to avoid `Key Error`. 
> * The first argument to get() is the key you want to retrieve, and the second argument is the default return value if the key is not found.

### Sum() for Sum with iterator in Python
> * Can use the sum() function to sum a certain operation over iterations in a loop.
> * Sum() takes an iterator as input in the form of:
`sum([action] for i in range ([number of times]))`
> * This will be the sum off all `[action]`s across `[number of times]` iterations