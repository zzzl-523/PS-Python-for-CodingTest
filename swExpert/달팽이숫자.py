# 3 2 2 1 1
# 4 3 3 2 2 1 1
# 이렇게 진행됨
d = [(1,0), (0,-1), (-1,0), (0,1)]

def solution(N):
    board = [[-1]*N for _ in range(N)]
    board[0] = [num for num in range(1, N+1)] # 첫 줄
    num = N
    d_cnt = -1
    x, y = 0, N-1
    for i in range(N-1, 0, -1):
        d_cnt = (d_cnt+1)%4
        
        for _ in range(i):
            nx, ny = x+d[d_cnt][0], y+d[d_cnt][1]
            num += 1
            board[nx][ny] = num
            x, y = nx, ny
        
        d_cnt = (d_cnt+1)%4
        for _ in range(i):
            nx, ny = x+d[d_cnt][0], y+d[d_cnt][1]
            num += 1
            board[nx][ny] = num
            x, y = nx, ny

    for i in range(N):
        for j in range(N):
            if j==N-1:
                print(board[i][j], end='\n')
            else: 
                print(board[i][j], end=' ')
        
    

T = int(input())

for t in range(1, T+1):    
    N = int(input())
    print("#"+str(t))
    solution(N)