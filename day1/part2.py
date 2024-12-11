from collections import Counter

left = []
right = []
with open("day1.txt") as f:
    for line in f.readlines():
        curr = line.strip().split("   ") # strip removes end line characters
        left.append(int(curr[0]))
        right.append(int(curr[1]))

right_count = Counter(right)

score = 0
for i in range(len(left)):
    score += left[i] * right_count.get(left[i],0)
    
print(score)