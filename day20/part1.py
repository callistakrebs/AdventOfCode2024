from collections import defaultdict, deque
import math
import numpy as np

CHEATCODE_LIMIT = 100

def is_in_bounds(position, nrows, ncols):
    return 0 <= position[0] < nrows and 0 <= position[1] < ncols

def build_graph(grid):
    graph = defaultdict(list)
    
    nrows = len(grid)
    ncols = len(grid[0])
    start_coord = -1
    end_coord = -1

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == "#":
                continue
            else:
                if grid[i][j] == "S":
                    start_coord = (i,j)
                if grid[i][j] == "E":
                    end_coord = (i,j)
                # left, right, up, down
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for neighbor in neighbors:
                    if is_in_bounds(neighbor, nrows, ncols) and grid[neighbor[0]][neighbor[1]] != "#":
                        graph[(i,j)].append(neighbor)
    
    return graph, start_coord, end_coord

def bfs(graph, start = (0,0)):
    queue = [start]
    visited = set([start])
    dist = {start: 0}
    path = []

    while queue:
        current = queue.pop(0)
        path.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited or dist[neighbor] > dist[current] + 1:
                dist[neighbor] = dist[current] + 1
                visited.add(neighbor)
                queue.append(neighbor)    
    
    return visited, dist,path

def get_path(prev, start_i, end_i):
    if prev[start_i][end_i] == None:
        return []

    path = []
    path.append(end_i)
    while start_i != end_i:
        end_i = int(prev[start_i][end_i])
        path.append(end_i)

    return path

if __name__ == "__main__":
    with open("day20.txt") as f:
        racetrack = [list(x) for x in f.read().split("\n")]

    # Build a graph of the input space, nodes are the positions in the racetrack, edges are between adjacent spaces that arent a wall
    # All edge weights are 1
    graph, start, end = build_graph(racetrack)

    # Get path with BFS
    _, dist, path = bfs(graph, start)

    # Get pairs that are 100 moves apart
    count = 0
    for i in range(len(path)):
        candidates = path[i + CHEATCODE_LIMIT + 2:]
        
        for candidate in candidates:
            if (path[i][0] == candidate[0]) and (abs(path[i][1] - candidate[1]) == 2):
                min_v = min(path[i][1], candidate[1])
                mid = min_v + 1

                if racetrack[path[i][0]][mid] == "#":
                    count += 1

            if (path[i][1] == candidate[1]) and (abs(path[i][0] - candidate[0]) == 2):
                min_v = min(path[i][0], candidate[0])
                mid = min_v + 1

                if racetrack[mid][path[i][1]] == "#":
                    count += 1

    print(count)