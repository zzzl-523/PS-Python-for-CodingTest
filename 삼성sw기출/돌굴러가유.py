# 돌의 개수 > 벽의 개수
# 벽이 설치된 마을부터는 돌이 구르지 않음
# N:마을의 개수, M:벽의 개수, K:돌의 개수

# 돌이 나오는 위치에 두는게 좋긴 함
# 돌이 나오고, 그 다음 돌이 나올 때까지는 계속 막히니까 ㄱㅊ
# 돌이 나오는 위치로 잡고, 최소가 되도록 구하기
# 돌의 개수에서 벽의 개수로 조합을 구해야 하는데, 이걸 다 구하면 25*24/2 => 300

import sys
from itertools import combinations
input = sys.stdin.readline

N, M, K = map(int, input().split())
morae_list = list(map(int, input().split()))
stones = list(map(int, input().split()))

# 벽의 개수 만큼 뽑기 -> 조합 
combs = list(combinations(stones, M))
min_value = 100000000
result = []
states = [0]*N

# 돌 굴러오는 위치 표시
for idx in stones:
    states[idx-1] = -1

# 벽 위치 표시
for combi in combs:
    temp_states = [num for num in states]

    for j in range(len(combi)):
        temp_states[combi[j]-1] = 1

    total = 0
    check = True
    for i in range(N):
        if temp_states[i] == -1:
            check = True
        elif temp_states[i] == 1:
            check = False
        
        if check:
            total += morae_list[i]
    
    if total < min_value:
        min_value = total
        result = [combi]
    elif total == min_value:
        result.append(combi)

result.sort()
print(*result[0], sep='\n')