n, m = map(int, input().split())
DP = []*n
maxi = 0

for i in range(n):
    DP.append(list(input()))   # string으로 처리

for i in range(1, n):
    for j in range(1, m):       
        if DP[i][j] == "1":
            if int(DP[i-1][j-1])>=1 and int(DP[i-1][j])>=1 and int(DP[i][j-1])>=1:
                DP[i][j] = str(min(int(DP[i-1][j-1]),int(DP[i-1][j]), int(DP[i][j-1])) + 1)
                    
for i in range(n):
    for j in range(m):
        maxi = max(maxi, int(DP[i][j]))
                
print(maxi*maxi)


