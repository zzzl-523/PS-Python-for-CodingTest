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

from collections import deque
q = deque

def solution(maps):
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
        return answer
    else:
        q.append(num_pos_list[0])

    # 상하좌우
    dxy = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def dfs(maps, x, y, visited, total):
        if visited[x][y]:
            return total
        visited[x][y] = True
        
        if maps[x][y] != 'X':
            total += int(maps[x][y])

        cnt = 0
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]

            if (0<=nx<len(maps) and 0<=ny<len(maps[0])) and not visited[nx][ny] and maps[nx][ny]!='X':
                dfs(maps, nx, ny, visited, total)
                cnt += 1

        # 이동할 곳 없을 때
        if cnt == 0:
            answer.append(total)
            if not num_pos_list:
                break
            nx = num_pos_list[0][0]
            ny = num_pos_list[0][1]
            if not visited[nx][ny]:
                q.append(num_pos_list[0])
            total = 0
        
        return total

    while q:
        x, y = q.popleft()

        dfs()

        # 시간..
        num_pos_list.remove((x, y))

        

    return sorted(answer)