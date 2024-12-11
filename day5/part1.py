from operator import itemgetter

def convert_pages(page_sets):
    return map(int, page_sets.split(","))

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

        # Check that each outgoing edge points to a later page in the list (verify topological sort)
        for i in range (len(group)):
            for page in subgraph[group[i]]:
                if page not in group[i+1:]:
                    valid = False
        
        if valid:
            valid_sum += group[int(len(group)/2)]
            
print(valid_sum)
        



