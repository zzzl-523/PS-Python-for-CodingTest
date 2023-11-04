import sys

input = sys.stdin.readline

N, M = map(int, input().split())
weight_arr = [-1]+list(map(int, input().split()))

# 친분관계 있으면, 그 사람보다 내가 더 무거운 거 들 수 있으면 내가 최고라고 생각함
# 없으면 걍 내가 최고

best_arr = [True]*(N+1)

for i in range(M):
  a, b = map(int, input().split())
  
  if weight_arr[a] < weight_arr[b]:
    best_arr[a] = False
    if best_arr[b]:
      best_arr[b] = True
  elif weight_arr[a] > weight_arr[b]: # 같은 경우는 없음
    best_arr[b] = False
    if best_arr[a]:
      best_arr[a] = True
  elif weight_arr[a] == weight_arr[b]:
    best_arr[a], best_arr[b] = False, False
    

answer = 0
for i in range(1, N+1):
  if best_arr[i]:
    answer += 1

print(answer)