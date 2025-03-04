from collections import defaultdict
import math

DIRECTIONS = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1),
}

def is_in_bounds(position):
    return 0 <= position[0] < 71 and 0 <= position[1] < 71

def build_graph(lava):
    '''
    builds the graph
    lava: list of tuples of (x,y) positions where the bytes will fall, making them unusable
    '''

    graph = defaultdict(list)

    for i in range(71):
        for j in range(71):
            if (i,j) in lava[0:1024]:
                continue
            else:
                # left, right, up, down
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for neighbor in neighbors:
                    if is_in_bounds(neighbor) and neighbor not in lava[0:1024]:
                        graph[(i,j)].append(neighbor)

    return graph

def bfs(graph, start = (0,0)):
    queue = [start]
    visited = set([start])
    dist = {start: 0}

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited or dist[neighbor] > dist[current] + 1:
                dist[neighbor] = dist[current] + 1
                visited.add(neighbor)
                queue.append(neighbor)    
    
    return visited, dist


if __name__ == "__main__":
    with open("day18.txt") as f:
        lava = [tuple(int(y) for y in x.split(",")) for x in f.read().split("\n")]

    graph = build_graph(lava)

    _, dist = bfs(graph)

    print(dist[(70,70)])
