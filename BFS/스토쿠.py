# 3가지 경우를 확인해야함
# 1. 가로
# 2. 세로
# 3. 네모(3x3)
# 확인하고 1~9 중 해당 경우에 없는 것을 배열에 저장
# 나머지 경우를 확인하면서 겹치는 것만 남기기
# 해결되지 않는 경우도 있는데,,
# 1트만에 해결되지 않으면 다시 큐에 넣기!

import time
start_time = time.time()
from collections import deque
import sys
input = sys.stdin.readline

N = 9
sudoku = [list(map(int, input().split())) for _ in range(9)]
blank_list = []
init_list = list(range(1, 10))

for i in range(N):
    count = sudoku[i].count(0)
    for j in range(N):
        if sudoku[i][j] == 0:
            blank_list.append(((i, j), count))


blank_list = sorted(blank_list, key=lambda x:x[1])

queue = deque(blank_list)
print(blank_list)
while queue:
    A = queue.popleft()[0]
    # print(A)
    x, y = A[0], A[1]

    # 3가지 경우 확인하기
    # 가로
    maybe_list = []
    sudoku_garo = sudoku[x]
    for num in init_list:   
        if num not in sudoku_garo:
            maybe_list.append(num)
    if len(maybe_list) == 1:
        print(maybe_list)
        sudoku[x][y] = maybe_list[0]
        continue
    
    # 세로
    maybe_list = []
    sudoku_sero = [i[y] for i in sudoku]
    for num in maybe_list:   
        if num not in sudoku_sero:
            maybe_list.append(num)
    if len(maybe_list) == 1:
        sudoku[x][y] = maybe_list[0]
        continue

    # 네모
    maybe_list = []
    sudoku_nemo = [sudoku[i][3*(y//3):3*(y//3)+3] for i in range(3*(x//3), 3*(x//3)+3)]
    sudoku_nemo = sum(sudoku_nemo, [])
    for num in maybe_list:   
        if num not in sudoku_nemo:
            maybe_list.append(num)
    if len(maybe_list) == 1:
        sudoku[x][y] = maybe_list[0]
        continue

    else:
        queue.append(((x, y), 0))

for i in range(N):
    for j in range(N):
        print(sudoku[i][j], end=' ')
    print()

end_time = time.time()
print('시간: ', end_time-start_time)