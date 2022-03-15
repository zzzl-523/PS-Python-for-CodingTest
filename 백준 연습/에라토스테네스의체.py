import math

N, K = map(int, input().split())
array = [True] * (N+1)
cnt = 0
num = 0

for i in range(2, N+1):
    if array[i] == True:
        j = 1 # 자신도 지운다
        while i*j <= N:
            if array[i*j] == True:
                array[i*j] = False  
                cnt += 1          
                if cnt == K:
                    num = i*j
                    break
                
            j += 1
    if cnt == K:
        break                

print(num)