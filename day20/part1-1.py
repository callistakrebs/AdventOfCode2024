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

def floyd_warshall(graph):
    nv = len(graph)

    # map vertices to integers
    vertex_map = {}
    integer_map = {}
    for idx, vertex in enumerate(graph):
        vertex_map[vertex] = idx
        integer_map[idx] = vertex

    dist = np.ones(shape=(len(graph), len(graph))) * np.inf
    prev = np.empty(shape=(len(graph), len(graph)), dtype=int)

    for node in graph:
        v = vertex_map[node]
        dist[v][v] = 0
        prev[v][v] = v
    
    for node in graph:
        for edge in graph[node]:
            v = vertex_map[node]
            u = vertex_map[edge]
            dist[u][v] = 1
            prev[u][v] = u

    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    return dist, prev, vertex_map, integer_map

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

    # All Pairs shortest path - Floyd Warshall
    apsp, prev, v_map, i_map = floyd_warshall(graph)

    # Get all pairs whose path is at least 100
    candidates = apsp >= CHEATCODE_LIMIT
    finishing_path = get_path(prev, v_map[start], v_map[end])

    # Filter for pairs you can add an edge to (i.e. there is a wall separating them)
    # Same row and column differs by 2 or same column and row differs by 2
    count = 0
    cheat_positions = set()
    for i in range(candidates.shape[0]):
        for j in range(candidates.shape[1]):
            if i == j:
                continue
            if not candidates[i][j]:
                continue
            if i not in finishing_path or j not in finishing_path:
                continue
            
            u = i_map[i]
            v = i_map[j]

            # Same row, col is 2 apart
            if ((u[0] == v[0] and abs(u[1] - v[1]) == 2)) and ((u,v) not in cheat_positions) and ((v,u) not in cheat_positions):
                max_v = max(u[1],v[1])
                min_v = min(u[1],v[1])
                mid = min_v + ((max_v - min_v) // 2)

                if racetrack[u[0]][mid] == "#":
                    count += 1
                    cheat_positions.add((u,v))

            # Same col, row is 2 apart
            if ((u[1] == v[1] and abs(u[0] - v[0]) == 2) and ((u,v) not in cheat_positions) and ((v,u) not in cheat_positions)):
                max_v = max(u[0],v[0])
                min_v = min(u[0],v[0])
                mid = min_v + ((max_v - min_v) // 2)

                if racetrack[mid][u[1]] == "#":
                    count += 1
                    cheat_positions.add((u,v))
                # graph[u].append(v)
                # graph[v].append(u)

                # apsp, _, _ = floyd_warshall(graph)

    print(cheat_positions)
    print(count)
