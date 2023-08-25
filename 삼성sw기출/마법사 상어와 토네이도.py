# 골드3
# NxN 모래밭에서 연습
# 좌표는 r, c
# A[r][c] -> 해당 칸의 모래 양

# 토네이도 시전하면 격자 가운데 칸부터 이동 시작
# 한 번에 한 칸 이동

# 토네이도가 이동하면, 해당 칸의 모든 모래가 비율과 a가 적혀있는 칸으로 이동
# 비율 칸으로 이동하는 모래의 양은 해당 비율 만큼
# a는 남은 만큼
# 이미 모래 있는 칸으로 가면, 모래의 양은 더해짐

# 토네이도 소멸 후 격자의 밖으로 나간 모래의 양 구하기!

# <풀이 전략>
# 1. 흩날리는 모래 비율 적힌 것을 이차원 배열(행렬)로 만들어서 그대로 곱해버리면 ..?
# 2. 달팽이처럼 나가는 거 어떻게 해결할까! 
    # 위치 이동은 
    # 1칸 왼, 아래
    # 2칸 오른, 위
    # 3칸 왼, 아래
    # 4칸 오른, 위 ...
    # (1, 1)에 도달할 때까지!


import sys
input = sys.stdin.readline

N = int(input())
matA = [list(map(int, input().split())) for _ in range(N)]
matB = [
    [0, 0, 2, 0, 0],
    [0, 10, 7, 1, 0],
    [5, -1, 0, 0, 0],
    [0, 10, 7, 1, 0],
    [0, 0, 2, 0, 0,]
]
result = 0

# 특정 좌표의 모래 양을 matB를 곱해서 나눠주는 함수
def mul(morae, pos):
    global result
    global matB
    global matA
    global N

    x, y = pos
    new_mat = matA.copy() # 얕은 복사 -> new_mat 변경하면 matA도 변경됨!

    num = len(matB)//2
    alpha = (0, 0)
    total = 0
    out_morae = 0
    for i in range(x-num, x+num+1):
        for j in range(y-num, y+num+1):
            if (i, j)== (x, y):
                new_mat[i][j] = 0
            if j < 0 or j >= N or i < 0 or i >= N:
                if matB[i-(x-num)][j-(y-num)] == -1:
                    alpha = (-1, -1)
                    continue
                out_morae += int(morae * matB[i-(x-num)][j-(y-num)]/100)
                continue
        
            if matB[i-(x-num)][j-(y-num)] == -1:
                alpha = (i, j)
                continue
            new_mat[i][j] += int(morae * matB[i-(x-num)][j-(y-num)]/100)
            total += int(morae * matB[i-(x-num)][j-(y-num)]/100)

    total += out_morae

    if alpha == (-1, -1):
        out_morae += morae - total
    else:
        new_mat[alpha[0]][alpha[1]] += morae - total

    result += out_morae

    return new_mat




# matrix를 왼쪽으로 90도씩 회전시키는 함수
def rotate():
    global matB
    for i in range(len(matB)):
        matB[i].reverse()
    matB = list(map(list, zip(*matB)))

    return matB

# 초기의 x, y는 중심부터 시작
x, y = N//2, N//2

move = 0
cnt = 0
while x>=0 and y>=0:
    if x<=0 and y<=0:
        break

    cnt += 1
    if cnt%2 == 1:
        move += 1
    
    if cnt > 1:
        rotate()
    
    for i in range(move):
        if move%2 == 1:
            if cnt %2 == 1: # left
                y -= 1
            else:           # down
                x += 1
        else:
            if cnt %2 == 1: # right
                y += 1
            else:           # up
                x -= 1

        mul(matA[x][y], (x, y))
    


print(result)