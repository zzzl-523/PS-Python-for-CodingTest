T = int(input())

for _ in range(T):
    N = int(input())
    DP = [0]*(N+10)
    DP[0] = 1
    DP[1] = 1
    DP[2] = 1
    DP[3] = 2
    DP[4] = 2
    DP[5] = 3
    DP[6] = 4
    DP[7] = 5
    DP[8] = 7
    DP[9] = 9

    for i in range(10, N):
        DP[i] = DP[i-1] + DP[i-5]

    print(DP[N-1])