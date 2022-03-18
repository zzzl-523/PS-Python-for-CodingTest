from collections import deque

N, L, R = map(int, input().split())
data = []

sum = 0
c_cnt = 1
day = 0
changed = False
avg = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    data.append(list(map(int, input().split())))

while True:
    index = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                c_cnt = 1
                sum = data[i][j]
                q = deque()
                q.append((i, j))
                new_q = deque()
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    new_q.append((x, y))

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                    
                        if nx>=0 and nx<N and ny>=0 and ny<N :
                            if (L<=abs(data[x][y] - data[nx][ny])<=R) and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                sum += data[nx][ny]
                                c_cnt += 1
                                              
                
                avg = int(sum/c_cnt)
                while new_q:
                    x, y = new_q.popleft()
                    data[x][y] = avg    

                index+=1       

    # 더 이상 돌아도 인구 이동 없을 때까지                    
    if index == N*N:
        break
    day += 1

print(day)
            