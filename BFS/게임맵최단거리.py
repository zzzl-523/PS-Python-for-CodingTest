from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def BFS(maps, start):
    queue = deque()
    queue.append(start) #(x,y)
    n = len(maps) # x축
    m = len(maps[0]) # y축
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx<0 or nx>m-1 or ny<0 or ny>n-1:
                continue
            if maps[ny][nx] == 1:
                queue.append((ny,nx))
                maps[ny][nx] = maps[y][x] + 1
            
    return maps[n-1][m-1]
        

def solution(maps):
    answer = BFS(maps, (0,0))
    if answer <= 1:
        answer = -1
    return answer