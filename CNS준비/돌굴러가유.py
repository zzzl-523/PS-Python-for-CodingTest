# 돌의 개수 > 벽의 개수
# 벽이 설치된 마을부터는 돌이 구르지 않음
# N:마을의 개수, M:벽의 개수, K:돌의 개수

# 돌이 나오는 위치에 두는게 좋긴 함
# 돌이 나오고, 그 다음 돌이 나올 때까지는 계속 막히니까 ㄱㅊ
# 돌이 나오는 위치로 잡고, 최소가 되도록 구하기
# 돌의 개수에서 벽의 개수로 조합을 구해야 하는데, 이걸 다 구하면 25*24/2 => 300

# 돌과 벽에 의해 영향 받는 구역을 벽 개수로 나눌 수 있음 -> 영향 구역 수는 돌 개수와 같음

import sys
from itertools import combinations
input = sys.stdin.readline

N, M, K = map(int, input().split())
morae_list = list(map(int, input().split()))
stones = list(map(int, input().split()))

# 돌 시작되는 위치로 구역 나누기
arr = [(-1, -1)]*K # 마을 번호, 부서지는 모래성 수
for idx in range(len(stones)):
    if idx == len(stones)-1:
        arr[idx] = (stones[idx], sum(morae_list[stones[idx]-1:]))
    else: arr[idx] = (stones[idx], sum(morae_list[stones[idx]-1:stones[idx+1]-1]))

# 피해 모래성 최소로 하는 벽 구하기
arr.sort(key=lambda x: (-x[1], x[0]))
arr = arr[:M]
arr.sort(key=lambda x: x[0])

for num in arr:
    print(num[0])