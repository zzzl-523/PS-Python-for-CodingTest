import itertools

N, K = map(int, input().split())
data = []

for i in range(N+1):
    data.append(i)

sum = 0
cnt = 0 # 총 경우의 수
for x in itertools.product(data, repeat = K):
    sum = 0
    for num in list(x):
        sum += num
    if sum == N:
        cnt += 1

print(cnt%1000000000)