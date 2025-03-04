from collections import defaultdict, deque

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

GRID_SIZE = 71  # Avoid magic numbers

def is_in_bounds(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

def build_graph():
    """
    Builds the initial graph of the entire grid.
    """
    graph = defaultdict(list)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            for dx, dy in DIRECTIONS.values():
                ni, nj = i + dx, j + dy
                if is_in_bounds(ni, nj):
                    graph[(i, j)].append((ni, nj))

    return graph

def delete_node(graph, node):
    """
    Removes a node from the graph and cleans up references in neighbors.
    """
    if node in graph:
        for neighbor in graph[node]:  # Remove the node reference from neighbors
            graph[neighbor].remove(node)
        del graph[node]  # Delete the node itself

def bfs(graph, start=(0, 0)):
    """
    Standard BFS to find shortest paths from `start`.
    """
    if start not in graph:  # If starting point is already lava, return empty
        return set(), {}

    queue = deque([start])
    visited = {start}
    dist = {start: 0}

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                dist[neighbor] = dist[current] + 1
                visited.add(neighbor)
                queue.append(neighbor)

    return visited, dist

if __name__ == "__main__":
    with open("day18.txt") as f:
        lava = [tuple(map(int, line.split(","))) for line in f.read().strip().split("\n")]

    graph = build_graph()
    _, dist = bfs(graph)

    if (70, 70) not in dist:
        print("Already unreachable before any lava!")
    else:
        for position in lava:
            delete_node(graph, position)

            # Skip BFS if the deleted node was already unreachable
            if position not in dist:
                continue

            _, dist = bfs(graph)

            if (70, 70) not in dist:
                print(position)
                break
