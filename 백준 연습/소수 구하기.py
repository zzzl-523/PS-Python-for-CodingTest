import math

M, N = map(int, input().split())
array = [True]*(N+1)
array[1] = False # 1은 소수 아님

for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1

for i in range(M, N+1):
    if array[i] == True:
        print(i)
