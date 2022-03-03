from collections import deque
t = int(input())
cnt = 0
dy = [-1, 0, 1]
dx = [1, 1, 1]

next_data = []
next_data.append((1,1))
while(True):
    cnt += 1
    if cnt > t:
        break
    n, m = map(int, input().split())
    graph = [[0]*(m+1) for _ in range(n+1)]
    DP = [[0]*(m+1) for _ in range(n+1)]

    data = list(map(int, input().split()))

    for i in range(1, n+1):
        for j in range(1, m+1):
            graph[i][j] = data[(i-1)*m + (j-1)]
            DP[i][j] = data[(i-1)*m + (j-1)]

    for x in range(1, m):
        for y in range(1, n+1):
            
            for i in range(3):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx>0 and nx<=m and ny>0 and ny<=n:
                    DP[ny][nx] = max(DP[y][x]+graph[ny][nx], DP[ny][nx])
            

    maxi = 0
    for i in range(1, n+1):
        if maxi < DP[i][m]:
            maxi = DP[i][m]

    print(maxi)


