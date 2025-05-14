from collections import defaultdict, deque
import math
import numpy as np

TIME_SAVED_MIN = 100

def is_in_bounds(position, nrows, ncols):
    return 0 <= position[0] < nrows and 0 <= position[1] < ncols

def build_graph(grid, walls=True):
    graph = defaultdict(list)
    
    nrows = len(grid)
    ncols = len(grid[0])
    start_coord = -1
    end_coord = -1

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == "#" and walls:
                continue
            else:
                if grid[i][j] == "S":
                    start_coord = (i,j)
                if grid[i][j] == "E":
                    end_coord = (i,j)
                # left, right, up, down
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for neighbor in neighbors:
                    if walls:
                        if is_in_bounds(neighbor, nrows, ncols) and grid[neighbor[0]][neighbor[1]] != "#":
                            graph[(i,j)].append(neighbor)
                    else:
                        if is_in_bounds(neighbor, nrows, ncols):
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
    walled_graph, start, end = build_graph(racetrack)

    unwalled_graph, start, end = build_graph(racetrack, walls=False)


    # Get path with BFS
    _, dist, path = bfs(walled_graph, start)

    # Get pairs that are 100 moves apart
    count = 0
    bfs_cache = {}
    for i in range(len(path)):
        print(f"{i} / {len(path)} iteration")
        candidates = path[i + TIME_SAVED_MIN:]
        
        for candidate in candidates:
            # Find a path between these in the unwalled graph that is at most length of max_cheat
            # if path[i] not in bfs_cache.keys():
            #     _, bfs_cache[path[i]], _ = bfs(unwalled_graph, path[i])

            curr_distance = path.index(candidate) - i # how far apart these nodes are in the path
            cheat_distance = abs(path[i][0]-candidate[0]) + abs(path[i][1]-candidate[1])

            if cheat_distance <= 20 and (curr_distance - cheat_distance >= TIME_SAVED_MIN):
                count += 1

    print(count)