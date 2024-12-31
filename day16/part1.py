from collections import defaultdict
import math
import heapq

DIRECTIONS = {
    'north': (-1,0),
    'south': (1,0),
    'west': (0,-1),
    'east': (0,1),
}

ALLOWED_MOVES = {
    'north': {'west':1001, 'north':1, 'east':1001},
    'east': {'north':1001, 'east':1, 'south':1001},
    'south': {'east':1001, 'south':1, 'west':1001},
    'west': {'north':1001, 'west':1, 'south':1001}
}

def is_in_bounds(grid, r,c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dijkstras(graph, start):
    dist = {}

    for node in graph:
        dist[node] = math.inf

    dist[start] = 0

    # Priority Queue
    pq = [(0,start)]
    heapq.heapify(pq)

    visited = set()
    while pq:
        weight, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist


if __name__ == "__main__":
    with open("day16.txt") as f:
        maze = [list(x) for x in f.read().split("\n")]
    
    nrows = len(maze)
    ncols = len(maze[0])

    graph = defaultdict(list)
    for r in range(nrows):
        for c in range(ncols):
            if maze[r][c] == "S":
                start = ((r,c), 'east')
            if maze[r][c] =="E":
                end_idx = (r,c)

            for curr_direction in DIRECTIONS:
                graph[((r,c),curr_direction)] = []
                for next_direction in ALLOWED_MOVES[curr_direction]:
                    dr, dc = DIRECTIONS[next_direction]
                    weight = ALLOWED_MOVES[curr_direction][next_direction]
                    if is_in_bounds(maze, r + dr, c + dc):
                        if maze[r+dr][c+dc] == "." or maze[r+dr][c+dc]== "E":
                            graph[((r,c),curr_direction)].append((((r+dr,c+dc), next_direction), weight))

    distances = dijkstras(graph, start)
    min = math.inf
    for direction in DIRECTIONS:
        if distances[(end_idx, direction)] <= min:
            end_state = (end_idx, direction)
            min = distances[(end_idx, direction)]
    
    print(min)
