from collections import deque
q = deque

maps = ["XXX","XXX","XXX"]

answer = []
num_pos_list = []
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] != 'X':
            num_pos_list.append((i, j))
            

visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
q = deque([])
total = 0

if len(num_pos_list)==0:
    answer.append(-1)
    print(answer)
    exit()
else:
    q.append(num_pos_list[0])

# 상하좌우
dxy = [(-1,0), (1,0), (0,-1), (0,1)]

while q:
    x, y = q.popleft()

    if visited[x][y]:
        continue
    visited[x][y] = True

    # 시간..
    num_pos_list.remove((x, y))
    
    if maps[x][y] != 'X':
        total += int(maps[x][y])

    cnt = 0
    for i in range(4):
        nx = x + dxy[i][0]
        ny = y + dxy[i][1]
    
        if (0<=nx<len(maps) and 0<=ny<len(maps[0])) and not visited[nx][ny] and maps[nx][ny]!='X':
            q.append((nx, ny))
            cnt += 1
        
    # 이동할 곳 없을 때
    if cnt == 0:
        print(total)
        answer.append(total)
        if not num_pos_list:
            break
        nx = num_pos_list[0][0]
        ny = num_pos_list[0][1]
        if not visited[nx][ny]:
            q.append(num_pos_list[0])
        total = 0

print(answer)

        