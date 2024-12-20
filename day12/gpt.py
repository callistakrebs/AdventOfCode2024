from collections import deque

DIRECTIONS = [
    (-1, 0),  # up
    (0, -1),  # left
    (1, 0),   # down
    (0, 1),   # right
]

DIAGONALS = [
    (-1, -1),  # up-left
    (-1, 1),   # up-right
    (1, -1),   # down-left
    (1, 1),    # down-right
]


def is_in_bounds(garden, r, c):
    return 0 <= r < len(garden) and 0 <= c < len(garden[0])


def get_cost(plots):
    return sum(len(plot["locations"]) * plot["corners"] for plot in plots)


def get_neighbors(garden, start, visited):
    queue = deque([start])
    current_plot = set()
    visited.add(start)
    letter = garden[start[0]][start[1]]

    while queue:
        r, c = queue.popleft()
        current_plot.add((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if is_in_bounds(garden, nr, nc) and garden[nr][nc] == letter and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))

    return current_plot


def count_corners(locations):
    corners = 0
    location_set = set(locations)

    for r, c in locations:
        fence_needed = [
            (r + dr, c + dc) not in location_set
            for dr, dc in DIRECTIONS
        ]

        # Count corners formed by two fences meeting
        for (idx1, idx2) in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            if fence_needed[idx1] and fence_needed[idx2]:
                corners += 1

        # Check diagonal fences
        for (dr, dc), (idx1, idx2) in zip(DIAGONALS, [(0, 1), (0, 3), (2, 1), (2, 3)]):
            if (r + dr, c + dc) not in location_set and not (fence_needed[idx1] or fence_needed[idx2]):
                corners += 1

    return corners


def get_corners(plots):
    for plot in plots:
        plot["corners"] = count_corners(plot["locations"])
    return plots


if __name__ == "__main__":
    try:
        with open("day12.txt") as f:
            garden = f.read().strip().split("\n")
    except FileNotFoundError:
        print("Input file 'day12.txt' not found.")
        exit(1)

    nrows, ncols = len(garden), len(garden[0])
    visited = set()
    plots = []

    for row in range(nrows):
        for col in range(ncols):
            if (row, col) not in visited:
                locations = get_neighbors(garden, (row, col), visited)
                plots.append({
                    "letter": garden[row][col],
                    "locations": locations
                })

    plots_with_corners = get_corners(plots)
    print(get_cost(plots_with_corners))
