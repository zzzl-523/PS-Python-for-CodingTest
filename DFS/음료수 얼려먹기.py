n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def DFS(x, y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    
    # 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 표시
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1,y)
        DFS(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i, j)==True:
            result+=1

print(result)
