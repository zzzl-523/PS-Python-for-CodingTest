# 시간초과 뜸

N = int(input())

cnt= 0
stri= ''
check= 0

DP = [[] for _ in range(N+1)]

for i in range(10):
    DP[1].append(i)
    cnt += 1

for i in range(2, N+1):
    for k in range(1, 10):
        for j in range(len(DP[i-1])):
            if k <= DP[i-1][j]//(10**(i-2)):
                DP[i].append(k*(10**(i-1)) + DP[i-1][j])
                cnt += 1

print(cnt%10007)

