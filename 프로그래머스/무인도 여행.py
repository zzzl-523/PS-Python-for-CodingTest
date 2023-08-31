# BFS 느낌
# (0,0)부터 queue에 넣고
# popleft 했을 때 X면
# 상하좌우 가능한 것 queue에 추가
# 아니면 visit 기록 확인
# visit 기록 없으면 total += 숫자
# 

# 1.
# 2. 상하좌우 이동한 칸이 숫자면 합치기
# 2. visited 배열에 기록
# 3. 
# 더이상 없으면 answer 배열에 append

# from collections import deque
# q = deque

# def solution(maps):
#     answer = []
#     visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
#     q = deque([])
    

#     # 상하좌우
#     dxy = [(-1,0), (1,0), (0,-1), (0,1)]
    
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             if maps[i][j] != "X" and not visited[i][j] :
#                 total = 0
#                 q = [(i, j)]
                
#                 while q:
#                     x, y = q.pop()

#                     if visited[x][y]:
#                         continue

#                     visited[x][y] = True
#                     total += int(maps[x][y])

#                     for i in range(4):
#                         nx = x + dxy[i][0]
#                         ny = y + dxy[i][1]

#                         if (0<=nx<len(maps) and 0<=ny<len(maps[0])) and not visited[nx][ny] and maps[nx][ny]!='X':
#                             q.append((nx, ny))


#                 answer.append(total)
                    

#     return sorted(answer) if answer else [-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    col, row = len(maps), len(maps[0])
    visited = [[False]*row for _ in range(col)]
    
    answer = []
    
    for i in range(col) :
        for j in range(row) :
            if maps[i][j] != "X" and not visited[i][j] :
                period = 0
                q = [(j, i)]
                
                while q :
                    x, y = q.pop()
                    if visited[y][x] :
                        continue
                    visited[y][x] = True
                    period += int(maps[y][x])
                    
                    for k in range(4) :
                        ax, ay = x + dx[k], y + dy[k]
                        if -1 < ax < row and -1 < ay < col and maps[ay][ax] != "X" and not visited[ay][ax] :
                            q.append((ax, ay))
                    
                answer.append(period)
    
    return sorted(answer) if answer else [-1]