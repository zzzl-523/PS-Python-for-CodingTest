from collections import deque

T = int(input())
tc = [[] for _ in range(T)]

for i in range(T):
    I = int(input())
    o_x, o_y = map(int, input().split())
    n_x, n_y = map(int, input().split())
    tc[i].append(I)
    tc[i].append((o_x, o_y))
    tc[i].append((n_x, n_y))

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(T):
    I = tc[i][0]
    o_x, o_y = tc[i][1]
    n_x, n_y = tc[i][2]
    visited = [[False]*(I+1) for _ in range(I+1)]

    q = deque()
    q.append((o_x, o_y, 0))
    visited[o_x][o_y] = True
   
    while q:
        x, y, cnt = q.popleft()

        if x == n_x and y == n_y: # 종료
            print(cnt)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < I and ny >= 0 and ny < I:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny, cnt))
                    cnt -= 1

