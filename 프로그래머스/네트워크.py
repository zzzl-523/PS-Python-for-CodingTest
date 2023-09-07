n=6
computers=[[1, 0, 1, 1, 0, 0], 
            [0, 1, 0, 0, 1, 1], 
            [1, 0, 1, 1, 1, 1], 
            [1, 0, 1, 1, 1, 1], 
            [0, 1, 1, 1, 1, 1], 
            [0, 1, 1, 1, 1, 1]]

# 일단 전체 돌기
# visited 배열을 만들고, computers 배열 돌면서 하나씩 확인
# 확인할 때 dfs로 확인하면서 visited 표시.
#   1
# |   |
# 3 - 4
# | X |
# 5 - 6
# |   |
#   2

def dfs(i, visited, computers, n):
    # 종료 조건
    if i==n:
        return

    # 연결된 곳은 모두 방문 체크
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(j, visited, computers, n)
    
    return

def solution(n, computers):
    visited = [False]*n
    cnt = 0
    
    for i in range(n):
        if not visited[i]: # 새로운 덩어리일 때만 개수 세기
            cnt += 1

        visited[i] = True # 방문 체크

        dfs(i, visited, computers, n)

    print(cnt)
    return cnt

solution(n, computers)