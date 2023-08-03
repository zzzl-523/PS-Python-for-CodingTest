# 최소 며칠이 걸리는지 구해야 하므로 BFS (최단거리)

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 동서남북
dxy = [(0,1), (0,-1), (1,0), (-1,0)]

# 익은 토마토 리스트
tomato_list = [] 
# 익지 않은 토마토 개수
count = 0     
y, x = 0, 0  

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato_list.append((i, j))
        elif graph[i][j] == 0:
            count += 1

if count == 0:
    print(0)

else:
    queue = deque(tomato_list) # 토마토가 있는 index를 queue에 넣기     
    while queue:
        y, x = queue.popleft()

        for move in dxy:
            ny = y + move[0]
            nx = x + move[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
                count -= 1

    if count > 0:
        print(-1)
    else:
        print(graph[y][x]-1) # 1부터 시작되니까 -1 해준다