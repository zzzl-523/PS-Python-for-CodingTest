# 방의 상태가 주어졌을 때 청소하는 영역의 개수를 구하는 프로그램 작성하시오
# NxM 크기의 직사각형으로 나타냄
# 청소기는 바라보는 방향 있음 -> 동서남북

# 작동 프로세스
# 청소되지 않은 경우, 청소
# 주변 4칸 중 청소되지 않은 빈 칸 X
    # 후진 가능 -> 한 칸 후진, 1번으로 돌아가기
    # 후진 불가능 -> 작동 멈춤
# O
    # 반시계(왼쪽.서쪽) 회전
    # 앞 칸이 청소되지 않은 빈 칸이면 한 칸 전진
    # 1번으로 돌아감


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
# d 0123 북동남서
states = [list(map(int, input().split())) for _ in range(N)]
# 0 = 청소되지 않은 빈 칸, 1 = 벽

# 북동남서
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0

while True:
    if states[x][y] == 0:
        count += 1
        states[x][y] =  -1
    
    check = False
    for dir in dxy:
        if states[x + dir[0]][y + dir[1]] == 0:
            check = True
            break
    
    if check:
        d = (d-1)%4 # 반시계 90도 회전
        nx = x + dxy[d][0]
        ny = y + dxy[d][1]
        # if nx<0 or nx>=N-1 or ny<0 or ny>=M-1:
        #     continue
        if states[nx][ny] == 0:
            x = nx
            y = ny
        
    else:
        nx = x + dxy[(d+2)%4][0]
        ny = y + dxy[(d+2)%4][1]
        # if nx<0 or nx>=N-1 or ny<0 or ny>=M-1:
        #     break
        if states[nx][ny] <= 0: # 벽만 아니면 후진 가능
            x = nx
            y = ny
        else:
            break
          
print(count)