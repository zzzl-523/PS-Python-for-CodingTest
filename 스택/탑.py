# 왼쪽으로(앞쪽) 레이저 발사
# 송신한 탑보다 높이가 높은 탑만 수신 가능

# 뒤에서부터 확인
# 앞으로 가면서 가장 먼저 만나는 높이가 더 높은 탑 찾기
# 존재하면 몇 번째 기둥인지 출력, 없으면 0 출력

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
stack = []
results = [0]*N

for i in range(N):
    while stack:
        if stack[-1][1] > array[i]:
            results[i] = stack[-1][0] + 1
            break
        stack.pop()
    stack.append([i, array[i]])

print(*results)