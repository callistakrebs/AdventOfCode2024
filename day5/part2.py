from operator import itemgetter

def convert_pages(page_sets):
    return map(int, page_sets.split(","))

def dfs(subgraph):
    stack = []
    visited = {x:False for x in subgraph.keys()}

    for node in subgraph.keys():
        if not visited[node]:
            explore(node, subgraph, visited, stack)

    return stack

def explore(u, subgraph, visited, stack):
    visited[u] = True
    for v in subgraph[u]:
        if not visited[v]:
            explore(v, subgraph,visited,stack)
    stack.append(u)

with open("day5.txt") as f:
    [rules, pages_to_copy] = f.read().split("\n\n")
    rules = rules.split('\n')
    pages_to_copy = pages_to_copy.split('\n')
    
    pages_to_copy_int = []
    for group in pages_to_copy:
        pages_to_copy_int.append(list(map(int,group.split(","))))

    graph = {}
    # add nodes:
    for group in pages_to_copy_int:
        for page in group:
            if graph.get(page,-1) == -1: # u is in graph
                graph[page] = []

    # add edges
    for rule in rules:
        [u,v] = list(map(int, rule.split("|")))

        if graph.get(u,-1) != -1: # u is in graph
            graph[u].append(v)
        else:
            graph[u] = [v]
        
    valid_sum = 0
    invalid_sum = 0
    for group in pages_to_copy_int:
        valid = True
        # Create subgraph for group of pages
        subgraph = {}
        for page in group:
            subgraph[page] = []
            for node in graph[page]:
                if node in group:
                    subgraph[page].append(node)

        # Get topo sort, and compare to current sort
        topo = dfs(subgraph)
        topo.reverse()
        
        if topo == group:
            valid_sum += group[int(len(group)/2)]
        else:
            invalid_sum += topo[int(len(topo)/2)]

print(f"Valid: {valid_sum}")
print(f"Invalid: {invalid_sum}")