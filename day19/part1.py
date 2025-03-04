import numpy as np

if __name__ == "__main__":
    with open("day19.txt") as f:
        towels, designs = f.read().split("\n\n")
        designs = designs.split("\n")
        towels = set(x.strip() for x in towels.split(","))
    
    count = 0
    for design in designs:
        dp_array = [0] * (len(design)) # dp_array stores the number of "remaining stripes" that are unmatched at this point in the design
        
        if design[0] in towels:
            dp_array[0] = 0 # first stripe is fulfilled by an independent towel
        else:
            dp_array[0] = 1 # the first stripe must be accounted for

        for i in range(1,len(design)):
            dp_array[i] = dp_array[i-1] + 1
            for j in range(0,i+1):
                if (design[j:i + 1] in towels and dp_array[j-1] == 0):
                    dp_array[i] = 0
                    break
        
        if dp_array[-1] == 0:
            count+=1

    print(count)

                