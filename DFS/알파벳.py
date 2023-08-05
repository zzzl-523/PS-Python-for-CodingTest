import sys

r, c = list(map(int, sys.stdin.readline().split()))
graph = [[0 for x in range(c)] for x in range(r)]
for i in range(r):
    temp = sys.stdin.readline()
    for k in range(c):
        graph[i][k] = temp[k]

visited = [False for x in range(26)]

def dfs(x, y, visited, depth):
    global dist
    dist = max(dist, depth)
    n = graph[x][y]
    visited[ord(n)-65] = True
    adj_list = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    check = 0
    for point in adj_list:
        px = point[0]
        py = point[1]
        if px >= 0 and px < r and py >=0 and py < c:
            n = graph[px][py]
            if visited[ord(n)-65] == False:
                check += 1
                dfs(px, py, visited, depth + 1)
                visited[ord(n)-65]=False


global dist
dist = 0
dfs(0, 0, visited, 1)
print(dist)