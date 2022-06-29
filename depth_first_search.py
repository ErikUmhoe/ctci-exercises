from search_node import SearchNode

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def dfs(visited, graph, node, findNode):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor, findNode)


dfs(visited, graph, 'B', 'F')
if 'F' in visited:
    print('TRUE')
visited = set()
dfs(visited, graph, 'A', 'F')
if 'F' in visited:
    print('TRUE')

visited = set()
dfs(visited, graph, 'C', 'E')
if 'E' in visited:
    print('TRUE')
else:
    print('FALSE')
