# 다시 풀어보기
import sys

input = sys.stdin.readline
from math import sqrt

g, l = map(int, input().split())

divide = l // g  # a*b = l/g

# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b  # 최대공약수

    return gcd(b, a % b)


for a in range(int(sqrt(divide)), 0, -1):  # 반대로 돌면서
    b = int(divide / a)  # b = (l/g)/a

    if divide % a == 0 and gcd(a, b) == 1:  # 약수고 서로소면
        print(a * g, b * g)
        break