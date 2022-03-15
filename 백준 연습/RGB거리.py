N = int(input())
DP = []
num = 0
temp = []

for i in range(N):
    temp = list(map(int, input().split()))
    DP.append(temp)

for i in range(1, N):
    for j in range(3):
        if j == 0:
            num = min(DP[i-1][1], DP[i-1][2])
            
        if j == 1:
            num = min(DP[i-1][0], DP[i-1][2])

        if j == 2:
            num = min(DP[i-1][1], DP[i-1][0])

        DP[i][j] = num + DP[i][j]

DP[N-1].sort()
print(DP[N-1][0])
            