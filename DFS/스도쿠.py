# DFS, 백트래킹
import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])


def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: # 출력 후
            print(*i) 
        exit() # 강제 종료

    y, x = blank[n]
    sudoku_garo = sudoku[y]
    sudoku_sero = [i[x] for i in sudoku]
    sudoku_nemo = [sudoku[i][3*(x//3):3*(x//3)+3] for i in range(3*(y//3), 3*(y//3)+3)]
    sudoku_nemo = sum(sudoku_nemo, [])

    for num in range(1,10):
        check_garo = num not in sudoku_garo
        check_sero = num not in sudoku_sero
        check_nemo = num not in sudoku_nemo

        if check_garo and check_sero and check_nemo:
            sudoku[y][x] = num
            find(n+1)
            sudoku[y][x] = 0


find(0)