import sys
input = sys.stdin.readline

N = int(input())
RGB = []
INF = 2148000000
ans = INF
for _ in range(N):
    RGB.append(list(map(int, input().split())))

for k in range(3):
    # 1번째 비교
    DP = [[INF, INF, INF] for _ in range(N)]
    DP[0][k] = RGB[0][k]

    for i in range(1, N):
        DP[i][0] = RGB[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = RGB[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = RGB[i][2] + min(DP[i-1][0], DP[i-1][1])

    for i in range(3):
        if i != k:
            ans = min(ans, DP[-1][i])

print(ans)