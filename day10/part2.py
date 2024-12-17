from collections import defaultdict

def hike(grid, starting_point, peaks = None, rating = None):
    startr = starting_point[0]
    startc = starting_point[1]

    if peaks is None:
        peaks = defaultdict(int)

    for dr, dc in directions:
        newr, newc = startr + dr, startc + dc 
        if 0 <= newr <= len(grid) - 1 and 0 <= newc <= len(grid) - 1:
            if grid[newr][newc] == grid[startr][startc] + 1:
                if grid[newr][newc] == 9:
                    peaks[(newr, newc)] += 1
                else:
                    hike(grid, (newr,newc), peaks)
    return peaks

directions = [
    (0, -1), # up
    (0, 1), # down
    (-1, 0), #left
    (1, 0) #right

]

if __name__ == "__main__":
    with open("day10.txt") as f:
        grid = f.read().split("\n")
        grid = [list(map(int,list(row))) for row in grid]
    
    nrows = len(grid)
    ncols = len(grid[0])

    rating = {}
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == 0:
                peaks_nroutes = hike(grid, (r,c))
                rating[(r,c)] = sum(peaks_nroutes.values())

    print(sum(rating.values()))