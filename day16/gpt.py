from collections import defaultdict
import math
import heapq

DIRECTIONS = {
    'north': (-1, 0),
    'south': (1, 0),
    'west': (0, -1),
    'east': (0, 1),
}

ALLOWED_MOVES = {
    'north': {'west': 1001, 'north': 1, 'east': 1001},
    'east': {'north': 1001, 'east': 1, 'south': 1001},
    'south': {'east': 1001, 'south': 1, 'west': 1001},
    'west': {'north': 1001, 'west': 1, 'south': 1001}
}

def is_in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dijkstras(graph, start):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        weight, node = heapq.heappop(pq)
        if weight > dist[node]:
            continue
        
        for neighbor, move_weight in graph[node]:
            new_weight = weight + move_weight
            if dist[neighbor] > new_weight:
                dist[neighbor] = new_weight
                heapq.heappush(pq, (new_weight, neighbor))
    
    return dist

def construct_graph(maze):
    nrows, ncols = len(maze), len(maze[0])
    graph = defaultdict(list)
    
    for r in range(nrows):
        for c in range(ncols):
            if maze[r][c] == "S":
                start = (r, c)
            if maze[r][c] == "E":
                end_idx = (r, c)
            
            for curr_direction in DIRECTIONS:
                for next_direction, weight in ALLOWED_MOVES[curr_direction].items():
                    dr, dc = DIRECTIONS[next_direction]
                    if is_in_bounds(maze, r + dr, c + dc) and (maze[r + dr][c + dc] in [".", "E"]):
                        graph[((r, c), curr_direction)].append(((r + dr, c + dc), next_direction, weight))
    
    return graph, start, end_idx

if __name__ == "__main__":
    with open("day16.txt") as f:
        maze = [list(x.strip()) for x in f.read().split("\n") if x.strip()]
    
    graph, start, end_idx = construct_graph(maze)
    distances = dijkstras(graph, start)
    
    # Find the minimal distance to the end position
    min_distance = min(distances[(end_idx, direction)] for direction in DIRECTIONS)
    print(min_distance)
    print(graph)