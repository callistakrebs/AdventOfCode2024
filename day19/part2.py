import numpy as np

if __name__ == "__main__":
    with open("day19.txt") as f:
        towels, designs = f.read().split("\n\n")
        designs = designs.split("\n")
        towels = set(x.strip() for x in towels.split(","))
    
    count = 0
    for design in designs:
        dp_array = [0] * (len(design) + 1) # now instead this stores the number of ways to have 0 letters leftover?
        dp_counts = [0] * (len(design) + 1)
        design = "x" + design

        dp_counts[0] = 1
        if design[1] in towels:
            dp_array[1] = 0 # first stripe is fulfilled by an independent towel
            dp_counts[1] = 1
        else:
            dp_array[1] = 1 # the first stripe must be accounted for
            dp_counts[1] = 0

        for i in range(2,len(design)):
            dp_array[i] = dp_array[i-1] + 1
            for j in range(1,i+1):
                if (design[j:i + 1] in towels and dp_array[j-1] == 0):
                    dp_array[i] = 0 # it is possible to break down at this point
                    dp_counts[i] += dp_counts[j-1]
        
        if dp_array[-1] == 0:
            count+= dp_counts[-1]

    print(count)

    # g b b r
    # 0 0 0 0
    # 1 2 2 4

    # b g g r
    # 0 0 0 0
    # 1 1 1 1

    # b r w r r
    # 0 0 1 0 0
    # 1 2 0 2 2