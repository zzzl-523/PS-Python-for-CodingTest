import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
num = int(((N*(N-1)%10007)/K)%10007)
print(num)