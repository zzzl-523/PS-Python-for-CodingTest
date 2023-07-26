# 크기가 NxM인 지도
# 주사위의 전개도
# 지도의 좌표는 (r, c)
# 주사위는 지도 위에 윗 면이 1, 동쪽이 3인 상태로 놓여짐 (x, y)에

# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있음
# 지도의 각 칸에는 정수가 하나씩 쓰여 있음
# 이동한 칸에 쓰여진 수가 0이면, 주사위 바닥면에 쓰여진 수가 복사됨
# 0이 아닌 경우 칸에 쓰여진 수가 주사위 바닥면에 복사됨. -> 칸에 쓰여진 수는 0됨
# 주사위가 이동했을 때마다 상단에 쓰여진 값을 구하는 프로그램 작성하시오

# 주사위를 지도 밖으로 이동시키려는 것은 무시해야함

import sys
from collections import deque
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)] # 2차원 지도
commands = list(map(int, input().split()))


# 방향 벡터 - 동서북남 1234
dxy = [(0,0), (0, 1), (0, -1), (-1, 0), (1, 0)]
downUp = deque([0,0,0,0])
leftRight = [0,0]
# 남
# [5, 6, 2, 1]
# [4, 3]
# 북
# [2, 1, 5, 6]
# [4, 3]
# 서
# [4, 5, 3, 2]
# [6, 1]
# 동
# [3, 5, 4, 2]
# [1, 6]

for command in commands:
    nx = x + dxy[command][0]
    ny = y + dxy[command][1]

    if (nx<0 or nx>N-1) or (ny<0 or ny>M-1):
        continue
    
    if command == 1:
        n_lr = [downUp[0],downUp[2]]
        downUp = deque([leftRight[1], downUp[1], leftRight[0], downUp[3]])
    elif command == 2:
        n_lr = [downUp[2],downUp[0]]
        downUp = deque([leftRight[0], downUp[1], leftRight[1], downUp[3]])
    elif command == 3:
        n_lr = leftRight
        downUp.rotate(-1)
    elif command == 4:
        n_lr = leftRight
        downUp.rotate(1)

    leftRight = n_lr

    print(downUp[0])
    if maps[nx][ny] == 0:
        maps[nx][ny] = downUp[2]
    else : 
        downUp[2] = maps[nx][ny]
        maps[nx][ny] = 0
    
    x = nx
    y = ny



