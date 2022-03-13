N = int(input())
DP = [0]*(N+2)

DP[0] = 1
DP[1] = 2


for i in range(2, N):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N-1]%10007)
