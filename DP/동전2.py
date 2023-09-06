# 골드5
# N가지 종류의 동전 -> 가치의 합 K원
# 동전의 개수는 최소로
# 

import sys
input = sys.stdin.readline

# N가지 종류 동전, 가치의 합 = K
N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]

# i원을 만들기 위해 필요한 경우의 수
dp = [10001 for _ in range(K+1)]
dp[0] = 0

for i in range(1, K+1):
    for coin in coin_list:
        if i < coin: continue # coin 하나가 전체 값보다 더 커질수는 없음
        dp[i] = min(dp[i], dp[i-coin]+1) # 해당 coin을 하나 더했을 때 값과 비교 (동전 개수 최소로)

# 전체 가치가 10000이하이므로 1원짜리 동전으로 한 경우 동전개수가 10001이 넘어갈 수 없음
if dp[K] == 10001:print(-1)
else:print(dp[K])