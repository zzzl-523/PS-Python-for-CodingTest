def DFS(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

graph = []
visited = [False]*9
DFS(graph, 1, visited)