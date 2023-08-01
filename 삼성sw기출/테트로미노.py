# 4개짜리 폴리오미노 == 테트로미노
# 5가지 종류가 있다
# 대칭
# 1. 상하대칭 -> row만 -해주기
# 2. 좌우대칭 -> col만 -해주기
# 3. 상하좌우 대칭 -> row, col -해주기
# 회전
# 1. 오른쪽 90도 -> row만 -하고, x, y 위치 바꾸기
# 2. 180도 -> 상하좌우 대칭이랑 같음
# 3. 270도 -> col만 -하고, x,y 위치 바꾸기


import sys
import time
start_time = time.time()
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

tetrominos = [
    [(0,1), (0,2), (0,3)],
    [(0,1), (1,0), (1,1)],
    [(1,0), (2,0), (2,1)],
    [(1,0), (1,1), (2,1)],
    [(0,1), (0,2), (1,1)]
]

# 기본 - 상하대칭 - 좌우대칭 - 상하좌우대칭
flips = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
rotation = []
result = 0

max_list = []
max_num = max(max(paper))

for i in range(N):
    for j in range(M):
        p = (i,j)
        for tetromino in tetrominos:
            for idx3 in range(8):
                np = [p]
                max_check = False
                for idx in range(3):
                    if idx3 < 4:
                        np_x = p[0] + (tetromino[idx][0] * flips[idx3][0])
                        np_y = p[1] + (tetromino[idx][1] * flips[idx3][1]) 
                    elif idx3 == 4:
                        # 1. 오른쪽 90도 -> row만 -하고, x, y 위치 바꾸기
                        np_x = p[0] + (tetromino[idx][1] * flips[1][0])
                        np_y = p[1] + (tetromino[idx][0] * flips[1][1])
                    elif idx3 == 5:
                        # 3. 270도 -> col만 -하고, x,y 위치 바꾸기
                        np_x = p[0] + (tetromino[idx][1] * flips[2][0]) 
                        np_y = p[1] + (tetromino[idx][0] * flips[2][1])
                    elif idx3 == 6:
                        np_x = p[0] + (tetromino[idx][1] * flips[1][0]) * flips[1][0]
                        np_y = p[1] + (tetromino[idx][0] * flips[1][1]) * flips[1][1]
                    elif idx3 == 7:
                        np_x = p[0] + (tetromino[idx][1] * flips[1][0]) * flips[2][0]
                        np_y = p[1] + (tetromino[idx][0] * flips[1][1]) * flips[2][1]
                        
                    if np_x < 0 or np_x >= N or np_y < 0 or np_y >= M:
                        break
                    
                    np.append((np_x, np_y))

                if len(np) < 4:
                    continue
                total = 0
                for idx2 in range(4):
                    total += paper[np[idx2][0]][np[idx2][1]]
                
                result = max(total, result)
        
print(result)

end_time = time.time()
print("time: ", end_time-start_time)