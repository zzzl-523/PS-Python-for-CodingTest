# 골드4
# DP
# 칼로리의 합이 가장 크게 되는 경우
# 어떤 값을 DP 배열에 넣을지!

import sys
input = sys.stdin.readline

result = []
while True:
    # N=사탕종류, M=가진돈
    N, M = map(float,input().split())
    N, M = int(N), int(M*100)
    
    if N==0 and M==0:
        break
    
    candy_list = []
    for _ in range(N):
        c, p = map(float, input().split())
        candy_list.append([int(c), int(p*100)])


    # 돈-칼로리를 DP로
    DP = [0]*(10001)
    
    for i in range(1, M+1):
        for candy in candy_list:
            
            if i<candy[1]: continue

            DP[i] = max(DP[i], DP[i-candy[1]] + candy[0])
            

    result.append(DP[M])

print(*result, sep='\n')