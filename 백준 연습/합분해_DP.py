N, K = map(int, input().split())

DP = [[1]*200]*200

for i in range(200):
    DP[0][i] = i+1

for i in range(1, N):
    for j in range(1, K):
        DP[i][j] = DP[i][j-1] + DP[i-1][j]

print(DP[N-1][K-1]%1000000000)