import sys

# 시간 줄이는 방법
input = sys.stdin.readline
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

for num in sorted(num_list, reverse = True):
    print(num)