from collections import deque

N, K = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0,0을 1,1처럼 사용
list = []
for i in range(N):
    for j in range(N):
        if data[i][j] > 0:
            list.append((i, j, data[i][j], 0))

list.sort(key = lambda x:(x[2]))

q = deque(list)
index = 0
while q:
    x, y, virus, time = q.popleft()
    if S == time:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N:
            if data[nx][ny] == 0:          
                data[nx][ny] = virus
                q.append((nx, ny, virus, time+1))


print(data[X-1][Y-1])
        





