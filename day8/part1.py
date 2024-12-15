from collections import defaultdict
from itertools import combinations

def subtract_tuples(a:tuple, b:tuple):
    return (a[0]-b[0], a[1]-b[1])

def add_tuples(a:tuple, b:tuple):
    return (a[0]+b[0], a[1]+b[1])

with open("day8.txt") as f:
    grid = f.read().split("\n")

nrows = len(grid)
ncols = len(grid[0])

antennaes = defaultdict(list)
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] != ".":
            antennaes[grid[i][j]].append((i,j))

antinodes = set()
for antennae in antennaes:
    pairs = combinations(antennaes[antennae], r=2)
    for pair in pairs:
        distance = subtract_tuples(pair[0],pair[1])
        candidates = (add_tuples(pair[0],distance), subtract_tuples(pair[1], distance))

        if 0 <= candidates[0][0] <= nrows - 1 and 0 <= candidates[0][1] <= ncols - 1:
            antinodes.add(candidates[0])

        if 0 <= candidates[1][0] <= nrows - 1 and 0 <= candidates[1][1] <= ncols - 1:
            antinodes.add(candidates[1])

print(len(antinodes))