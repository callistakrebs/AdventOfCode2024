from collections import defaultdict

def hike(grid, starting_point, peaks=None):
    if peaks is None:
        peaks = defaultdict(int)

    startr, startc = starting_point

    for dr, dc in DIRECTIONS:
        newr, newc = startr + dr, startc + dc
        if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]):
            if grid[newr][newc] == grid[startr][startc] + 1:
                if grid[newr][newc] == 9:
                    peaks[(newr, newc)] += 1
                else:
                    # Recursively explore all paths
                    sub_peaks = hike(grid, (newr, newc))
                    for peak, count in sub_peaks.items():
                        peaks[peak] += count
    return peaks

DIRECTIONS = [
    (0, -1),  # up
    (0, 1),   # down
    (-1, 0),  # left
    (1, 0)    # right
]

if __name__ == "__main__":
    with open("day10.txt") as f:
        grid = [list(map(int, list(row))) for row in f.read().strip().split("\n")]

    nrows, ncols = len(grid), len(grid[0])

    ratings = {}
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == 0:
                peaks_nroutes = hike(grid, (r, c))
                ratings[(r, c)] = sum(peaks_nroutes.values())

    print(f"Total distinct routes to peaks: {sum(ratings.values())}")
