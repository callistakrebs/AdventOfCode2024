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

def build_graph():
    '''
    builds the graph of the grid
    '''

    graph = defaultdict(list)

    for i in range(71):
        for j in range(71):
            # left, right, up, down
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for neighbor in neighbors:
                if is_in_bounds(neighbor):
                    graph[(i,j)].append(neighbor)

    return graph

def delete_node(graph, node):
    graph.pop(node)

    for node in graph:
        for idx, neighbor in enumerate(graph[node]):
            if neighbor == node:
                graph[node].pop(idx)

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

    # update graph building so that we build the whole grid, and then remove nodes that become lava
    graph = build_graph()

    # We can still use bfs, but need to run it each time we drop the bytes, and check if 70,70 is still in the distance dict after bfs
    for position in lava:
        graph = delete_node(graph, position)
        _, dist = bfs(graph)

        if (70,70) in dist:
            continue
        else:
            print(position)
            break

