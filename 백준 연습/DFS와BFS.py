from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)
ans_dfs = str(V) + " "
ans_bfs = str(V) + " "

for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()
    
def DFS(v):
    global ans_dfs
    visited_dfs[v] = True

    for node in graph[v]:
        if visited_dfs[node] == False:
            ans_dfs += str(node) + " "
            DFS(node)


def BFS(v):
    global ans_bfs
    q = deque(graph[v])
    visited_bfs[v] = True
    for i in graph[v]:
        visited_bfs[i] = True

    while q:
        vv = q.popleft()    
        ans_bfs += str(vv) + " "

        for node in graph[vv]:
            if visited_bfs[node] == False:
                visited_bfs[node] = True
                q.append(node)
                

DFS(V)
BFS(V)
print(ans_dfs)
print(ans_bfs)
