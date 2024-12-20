DIRECTIONS = [
    (-1,0), # up
    (0,-1), # left
    (1,0),  # down
    (0,1),  # right
]

def get_cost(plots):
    costs = []
    for plot in plots:
        area = len(plot[1])
        perimeter = plot[2]
        costs.append(area * perimeter)
    
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
                places, p = get_neighbors(garden, (row,col), visited=visited)
                plots.append((curr_letter, places, p))

    print(get_cost(plots))

