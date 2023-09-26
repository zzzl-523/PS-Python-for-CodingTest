# 공평하게 선거구 정하기
# 구역을 5개의 선거구로 나누기
# 각 구역은 반드시 5개 중 하나에 포함되어야 함
# 각 선거구도 반드시 구역을 1개 이상 포함해야 함
# 한 선거구 안 구역은 모두 연결되어 있어야 함

#  /이 방향끼리 d1, \이 방향끼리 d2
# 구역 (r, c)의 인구는 A[r][c]
# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값

# 내가 기준점(x,y), 경계의 길이(d1,d2) 구하는 것!

# (0,0)부터 돌면서 d1,d2==1부터 돌면서 확인하기. 

import sys
input = sys.stdin.readline

N = int(input())
A = [[0]]*N

for i in range(N):
    A[i] = list(map(int, input().split()))



def fill(x, y, d1, d2, N):
    maps = [[0 for _ in range(N)] for _ in range(N)]

    if x+d1+d2>N or y-d1<0 or y+d2>N:
        return

    # 채우기
    for i in range(N):
        for j in range(N):
            if i<x+d1 and j<=y:
                maps[i][j] = 1
            elif i<=x+d2 and j>y:
                maps[i][j] = 2
            elif i>=x+d1 and j<y-d1+d2:
                maps[i][j] = 3
            elif i>x+d2 and j>=y-d1+d2:
                maps[i][j] = 4

    
    for i in range(d1+1):
        # 경계선 1, 4
        maps[x+i][y-i] = 5
        maps[x+d2+i][y+d2-i] = 5
    
    for i in range(d2+1):
        # 경계선 2, 3
        maps[x+i][y+i] = 5
        maps[x+d1+i][y-d1+i] = 5
    
    # 5 채우기
    for i in range(x+1, x+d1+d2):
        for j in range(N):
            if j-1<=-1 or j+1>=N:
                continue
            
            if maps[i][j-1] == 5:
                if maps[i][j] == 5:
                    break
                maps[i][j] = 5
            
    return maps

def calculate(A, maps, N):
    arr = [0, 0, 0, 0, 0] 
    for i in range(N):
        for j in range(N):
            arr[maps[i][j]-1] += A[i][j]

    return max(arr) - min(arr)



min_value = 100000

for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(N):
            for y in range(1, N):
                if x+d1+d2>=N or y+d2>=N or y-d1<0 :
                    continue
                else:
                    result = calculate(A, fill(x, y, d1, d2, N), N)
                    min_value = min(result, min_value)
                    

print(min_value)