N = int(input())
cnt = 0
DP = [0]*1000005
DP[1] = 0
DP[2] = 1
DP[3] = 1
DP[4] = 2

a = 0
b = 0
c = 0
for i in range(5, N+1):
    a = 0
    b = 0
    c = 0
    if i % 3 == 0:
        a = DP[i//3] + 1
    if i % 2 == 0:
        b = DP[i//2] + 1       
    c = DP[i-1] + 1

    if a!=0 and b!=0 and c!=0:
        DP[i] = min(min(a, b), c)
    elif a!=0 and c!=0:
        DP[i] = min(a, c)
    elif c!=0 and b!=0:
        DP[i] = min(c, b)
    else:
        DP[i] = c

print(DP[N])