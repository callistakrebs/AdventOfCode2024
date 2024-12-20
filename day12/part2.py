DIRECTIONS = [
    (-1,0), # up
    (0,-1), # left
    (1,0),  # down
    (0,1),  # right
]

DIAGNOLS = {
    (-1,-1): "up-left", # up left
    (-1, 1): "up-right", # up right
    (1, -1): "down-left", # down left
    (1, 1):  "down-right"# down right
}


def is_in_bounds(garden, r,c):
    return 0 <= r < len(garden) and 0 <= c < len(garden[0])


def get_corners(plots):
    new_plots = []
    for idx,plot in enumerate(plots):
        corners = 0
        for r,c in plot["locations"]:
            fence_needed = [False, False, False, False] # up, left, down, right
            for idx,(dr, dc) in enumerate(DIRECTIONS):
                nr, nc = r + dr, c + dc
                if (nr,nc) not in plot["locations"]:
                    fence_needed[idx] = True
            
            corners += count_corners(fence_needed)

            for idx,(dr,dc) in enumerate(DIAGNOLS):
                nr, nc = r + dr, c + dc
                if (nr,nc) not in plot["locations"]:
                    if DIAGNOLS[(dr,dc)] == "up-left" and not fence_needed[0] and not fence_needed[1]:
                        corners += 1
                    if DIAGNOLS[(dr,dc)] == "up-right" and not fence_needed[0] and not fence_needed[3]:
                        corners += 1
                    if DIAGNOLS[(dr,dc)] == "down-left" and not fence_needed[1] and not fence_needed[2]:
                        corners += 1
                    if DIAGNOLS[(dr,dc)] == "down-right" and not fence_needed[3] and not fence_needed[2]:
                        corners += 1

        plot["corners"] = corners
        new_plots.append(plot)
    return new_plots

def count_corners(fence_needed):
    count = 0
    if fence_needed[0] and fence_needed[1]:
        count += 1
    if fence_needed[1] and fence_needed[2]:
        count += 1
    if fence_needed[2] and fence_needed[3]:
        count += 1
    if fence_needed[3] and fence_needed[0]:
        count += 1
    
    return count

def get_cost(plots):
    costs = []
    for plot in plots:
        area = len(plot["locations"])
        sides = plot["corners"]
        costs.append(area * sides)
    
    total_cost = sum(costs)

    return total_cost

def get_neighbors(garden, point, visited = None, current_plot = None, perimeter=0):
    if visited is None:
        visited = set()

    if current_plot is None:
        current_plot = set()

    if point in visited:
        return current_plot, perimeter

    visited.add(point)
    current_plot.add(point)

    for dr,dc in DIRECTIONS:
        nr, nc = point[0] + dr, point[1] + dc
        if 0 <= nr < len(garden) and 0 <= nc < len(garden[0]):
            if garden[point[0]][point[1]] == garden[nr][nc]:
                _, perimeter = get_neighbors(garden, (nr,nc), visited, current_plot, perimeter=perimeter)
            # If they dont match, this position is a boundary
            else:
                perimeter += 1
        else:
            perimeter +=1
    
    return current_plot, perimeter

if __name__ == "__main__":
    with open("day12.txt") as f:
        garden = f.read().split("\n")
    
    nrows = len(garden)
    ncols = len(garden[0])

    plots = [] # values are (letter, points included in the plot), area is the length of the set
    visited = set()
    for row in range(nrows):
        for col in range(ncols):
            if (row,col) not in visited:
                curr_letter = garden[row][col]
                places, perimeter = get_neighbors(garden, (row,col), visited=visited)
                plots.append({"letter":curr_letter,"locations":places, "perimeter":perimeter})

    plots_with_corners = get_corners(plots)
    print(get_cost(plots_with_corners))