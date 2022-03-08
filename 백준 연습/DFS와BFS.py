from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
visited_bfs = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

str_dfs = ''
str_bfs = ''

def DFS(graph, v, str_dfs, visited):
    visited[v] = True
    str_dfs += str(v)
    for n in graph[v]:
        if visited[n] == False:
            str_dfs += str(n)
            DFS(graph, n, str_dfs, visited)

def BFS(graph, v, str_bfs, visited_bfs):
    q = deque(graph[v])
    str_bfs += str(v)
    while q:
        n = q.popleft()
        if visited_bfs[n] == False:
            str_bfs += str(n)
            visited_bfs[n] = True
            q.append(graph[n])
            

DFS(graph, V, str_dfs, visited)
BFS(graph, V, str_bfs, visited_bfs)

