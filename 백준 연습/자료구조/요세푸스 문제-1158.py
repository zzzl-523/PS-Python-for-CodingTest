from collections import deque

N, K = map(int, input().split())
# queue 배열 만들기
ppl_list = deque([i for i in range(1, N+1)])
res_list = []

next_num = K
prev_idx = 0
prev_num = -1

# 방법1 -> 코드는 복잡하지만 시간이 훨씬 짧음
for _ in range(N):
    if len(ppl_list) == 1:
        res_list.append(ppl_list[0])
        break
    idx = (prev_idx + (K-1))%len(ppl_list)
    prev_idx = idx

    num = ppl_list[idx]
    
    res_list.append(num)
    ppl_list.remove(num)
    prev_num = num


# 방법2 -> 코드는 짧지만 시간이 10배 늘어남
# for _ in range(N):
#     for _ in range(K-1):
#         # K번째가 맨 앞에 오도록 그 앞 수들을 가장 뒤로 push하기
#         ppl_list.append(ppl_list.popleft())
#     res_list.append(ppl_list.popleft())
    
result = ''
for idx, num in enumerate(res_list):
    if idx == 0 and idx == len(res_list)-1:
        result += '<' + str(num) + '>'
        break
    if idx == 0:
        result += '<' + str(num) + ', '
    elif idx == len(res_list)-1:
        result += str(num) + '>'
    else:
        result += str(num) + ', '
print(result)