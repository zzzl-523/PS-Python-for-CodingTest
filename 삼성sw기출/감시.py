# 감시
# 스타트링크 사무실 -> NxM 사이즈
# 총 K개의 CCTV 설치되어 있음
# 각 CCTV마다 감시 방법 다름
    # 1번 : ->
    # 2번 : <- ->
    # 3번 : 위 -> (직각)
    # 4번 : <- 위 -> (ㅗ 모양)
    # 5번 : 네 방향 전부 (+ 모양)
# <조건>
    # 1. 벽은 통과 못함 (사각지대)
    # 2. 회전 가능 (90도 방향)
    # 3. 칸 개수는 상관 없음 (벽 닿을 때까지 계속)
    # 4. CCTV끼리는 통과 가능
# <지도>
    # 0 -> 빈 칸
    # 1~5 -> CCTV 번호
    # 6 -> 벽
    # # -> 감시 영역
# 구하는 것 : 사각지대 크기의 최소

import sys
readline = sys.stdin.readline

N, M = map(int, input().split()) # N-세로, M-가로
states = [list(map(int, input().split())) for _ in range(N)]

# 라이브러리 없이 deep copy를 하기 위한 함수
def copy(arr):
    copy = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy[i][j] = arr[i][j]
    return copy

# 일단 5가지 종류의 CCTV 만들기 (칸 개수는 for문으로 처리)
cctv_list = [
    [(0, 1)], # 1번 : ->
    [(0, -1), (0, 1)], # 2번 : <- ->
    [(-1, 0), (0, 1)], # 3번 : 위 -> (직각)
    [(0, -1), (-1, 0), (0, 1)], # 4번 : <- 위 -> (ㅗ 모양)
    [(0, -1), (-1, 0), (0, 1), (1, 0)] # 5번 : 네 방향 전부 (+ 모양)
]
# 90도 회전은 row*(-1)하고 row, column 뒤집기
# 180도 회전은 row*(-1), col*(-1)
# 270도 회전은 col*(-1)하고 row, col 뒤집기
# 회전 리스트 만들기
def rorate(A):
    # A = 각 CCTV
    A_rotates = [[] for _ in range(4)]
    for a in A:
        a_90 = (a[1], -a[0]) 
        a_180 = (-a[0], -a[1])
        a_270 = (-a[1], a[0])
        A_rotates[0].append(a)
        A_rotates[1].append(a_90)
        A_rotates[2].append(a_180)
        A_rotates[3].append(a_270)
    return A_rotates

# CCTV 위치 파악, 벽 개수 파악
pos_list = [] # CCTV 위치 리스트
wall_cnt = 0
for i in range(N):
    for j in range(M):
        if 0 < states[i][j] < 6:
            pos_list.append((i, j))
        if states[i][j] == 6:
            wall_cnt += 1

# 총 빈 칸 개수
total = N*M - len(pos_list) - wall_cnt
answer = total

# CCTV 기능에 따라 빈 칸 카운트 하는 함수
def count(cctv_pos, B, states_copy, result):
    cnt = result
    # print("B: ", B)
    for move in B:
        x, y = cctv_pos
        nx, ny = x, y
        while True:
            nx = x + move[0]
            ny = y + move[1]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                break 

            if states_copy[nx][ny] == 6: # 벽 만남
                break

            if states_copy[nx][ny] == 0:
                states_copy[nx][ny] = '#'
                cnt -= 1
            
            x, y = nx, ny
    
    return [cnt, states_copy]
        
# CCTV로 감시하는 칸 확인. 회전도 확인
def check(index, result, states_copy):
    global answer

    # 모든 CCTV 확인 끝나면 종료
    if index>len(pos_list)-1:
        # print('종료')
        return result

    pos = pos_list[index]
    num = states_copy[pos[0]][pos[1]]
    cctv = cctv_list[num-1]
    rotates = rorate(cctv)
    
    for i in range(4): # 모든 rotation에 대해 확인
        tmp_states = copy(states_copy) # 각 rotation에 따른 결과를 분리하기 위해 새롭게 deep copy
    
        cnt, tmp_states = count(pos, rotates[i], tmp_states, result)
        total_result = check(index+1, cnt, tmp_states)

        answer = min(answer, total_result) # min이면 answer 갱신

    return answer

print(check(0, total, copy(states)))