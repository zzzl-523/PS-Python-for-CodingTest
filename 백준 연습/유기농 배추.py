from collections import deque

T = int(input())
M, N, K = 0, 0, 0
data = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(y, x):
    q = deque()
    q.append((x, y))
    data[y][x] = 2 # 방문 표시

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and nx<M and ny>=0 and ny<N:
                if data[ny][nx] == 1:
                    q.append((nx, ny))
                    data[ny][nx] = 2 # 방문 표시


while(T>0):
    T -= 1 # 테스트케이스 횟수
    cnt = 0

    M, N, K = map(int, input().split())
    data = [[0]*M for _ in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        data[b][a] = 1

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)
    


    