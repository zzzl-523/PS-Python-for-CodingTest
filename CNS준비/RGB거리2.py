import sys
input = sys.stdin.readline

N = int(input())
DP = []
for i in range(N):
    DP.append(list(map(int, input().split())))

for i in range(1, N-1):
    for j in range(3):
        if j == 0:
            DP[i][j] += min(DP[i-1][1], DP[i-1][2])
        elif j == 1:
            DP[i][j] += min(DP[i-1][0], DP[i-1][2])
        elif j == 2:
            DP[i][j] += min(DP[i-1][0], DP[i-1][1])


for i in range(3):
    if i == 0:
        DP[N-1][i] += min(DP[(N-1)-1][1], DP[(N-1)-1][2])
    elif i == 1:
        DP[N-1][i] += min(DP[(N-1)-1][0], DP[(N-1)-1][2])
    elif i == 2:
        DP[N-1][i] += min(DP[(N-1)-1][0], DP[(N-1)-1][1])

print(min(DP[-1]))