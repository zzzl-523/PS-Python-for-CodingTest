# 영역구하기
# 왼쪽 아래는 그대로 포함, 오른쪽 위에는 -1,-1 해주기
# -로 바꾸고, -1 해주기

import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(K)]

boards = [[0 for _ in range(N)] for _ in range(M)]
print(*boards, sep='\n')
for point in points:
    print(M-point[1]-1, point[0], N-point[3], point[2]-1)
    boards[-point[1]-1][point[0]] = 1
    boards[-point[3]][point[2]-1] = 1

print(*boards, sep='\n')
