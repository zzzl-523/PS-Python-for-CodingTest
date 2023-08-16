import math
n = 1000 # 2부터 1000까지의 모든 소수 판별하기
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1): # 제곱근까지만 판별하면 된다
    if array[i] == True: # 남아 있는 수라면 (i가 소수라면)
        j = 2
        while i * j <= n: # i를 제외한 i의 모든 배수 지우기
            array[i*j] = False
            j += 1

# 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')