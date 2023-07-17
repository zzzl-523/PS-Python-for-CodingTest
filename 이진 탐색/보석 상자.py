import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
bosuk_list = [int(input()) for _ in range(M)]

result = max(bosuk_list)
l = 1
r = result

while l<=r:
    mid = (l+r)//2

    person_with_bosuk = 0
    for bosuk in bosuk_list:
        # 보석 개수를 mid로 나눠줌
        quotient = bosuk // mid # 몫은 보석을 나눠줄 수 있는 사람 수
        remainder = bosuk % mid # 나머지는 남은 보석 수

        person_with_bosuk += quotient
        if remainder > 0:
            person_with_bosuk += 1
    
    if person_with_bosuk > N: # 나눠주려는 사람 수가 실제 사람 수보다 많으면 더 큰 값으로 나눠주야 함
        l = mid + 1
    else: # 나눠주려는 사람 수가 더 적으면 한 사람 당 더 작은 수의 보석을 나눠줘도 된다는 뜻
        result = min(result, mid)
        r = mid - 1

print(result)