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

# 흩날리는 모래 비율 적힌 것을 이차원 배열(행렬)로 만들어서 그대로 곱해버리면 ..?

matA = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

matB = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# matB를 matA에 곱하는 함수 (element-wise)
def mul(matA, matB, pos):
    x, y = pos
    new_mat = matA.copy() # 얕은 복사 -> new_mat 변경하면 matA도 변경됨!
    num = int(len(matB)/2)
    for i in range(x-num, x+num+1):
        print(i)
        for j in range(y-num, y+num+1):
            print(j, end=' ')
            new_mat[i][j] += matA[i][j] * matB[i-(x-num)][j-(y-num)]
        print()

    print(*new_mat, sep='\n')
    return new_mat


# matrix를 왼쪽으로 90도씩 회전시키는 함수
def rotate(matB):
    for i in range(len(matB)):
        matB[i].reverse()
    matB = list(map(list, zip(*matB)))

    print(*matB, sep='\n')
    return matB

matB = rotate(matB)
matB = rotate(matB)
matB = rotate(matB)
matB = rotate(matB)

