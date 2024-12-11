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

sum = sum(abs(left[i] - right[i]) for i in range (len(left)))
    
print(sum)
