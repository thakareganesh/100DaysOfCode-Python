
# copper = {'species': 'guinea pig', 'age': 2}
"""
# print(copper['species'])
# print(copper['age'])

# Added new key-pair in dictionary
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
del copper['age']
print(copper)
"""

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), (' D', 7)],
    'D': [('A', 1), ('C', 7)]
    }

def shortest_path(graph,start):
    # unvisited = []
    unvisited = list(graph)
    # Dictionary comperahension with if-else
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Dictionary comperahension
    paths = {node: [] for node in graph}
    paths[start].append(start)
    # for node in graph:
    #     unvisited.append(node)
    #     if node == start:
    #         distances [node] = 0
    #     # float('inf') represent the positive infinity
    #     else:
    #         distances[node] = float('inf')
    print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

shortest_path(my_graph,'A')