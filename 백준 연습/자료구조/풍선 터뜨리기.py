# rotate
# 왼쪽으로 가서 -되면 해당 idx값 그대로 -로 사용
# 오른쪽 끝으로 가서 넘어가면 해당 idx값%N 값으로 사용
# 이미 터진 다음에는 0으로 바꿔주기 (0은 없으니까)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num_q = deque(enumerate(map(int, input().split())))
result = []

while num_q:
    idx, num = num_q.popleft()
    result.append(idx + 1)

    if num > 0:
        num_q.rotate(-(num - 1))
    elif num < 0:
        num_q.rotate(-num)

print(' '.join(map(str, result)))