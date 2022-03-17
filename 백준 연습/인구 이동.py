from collections import deque

N, L, R = map(int, input().split())
data = []
visited = [[False]*N for _ in range(N)]

sum = 0
c_cnt = 1
day = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            sum = data[0][0]
            q = deque()
            q.append((0, 0))
            new_q = deque()
            new_q.append((0, 0))

        elif L<=(sum-data[i][j])<=R:
            print(i, j)
            q.append((i, j))
            visited[i][j] = True
            
            
            while q:
                x, y = q.popleft()
                new_q.append((x, y))

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                   
                    if nx>=0 and nx<N and ny>=0 and ny<N :
                        if (L<=data[x][y] - data[nx][ny]<=R) and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            sum += data[nx][ny]
                            print(sum)
                            c_cnt += 1
            
            avg = sum/c_cnt
            while new_q:
                x, y = new_q.popleft()
                data[x][y] = avg

            day += 1

print(day)
            