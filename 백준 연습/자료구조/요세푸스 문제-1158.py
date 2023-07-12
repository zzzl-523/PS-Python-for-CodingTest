from collections import deque

N, K = map(int, input().split())
ppl_list = [i for i in range(1, N+1)]
res_list = []

next_num = K
prev_idx = 0
prev_num = -1

for _ in range(N):
    if len(ppl_list) == 1:
        res_list.append(ppl_list[0])
        break
    idx = prev_idx + (K-1)
    temp_list = ppl_list.copy()
    prev_idx = idx%len(ppl_list)

    if idx >= len(ppl_list) - 1:
        temp_list.extend(ppl_list[:K])
        idx = idx%len(ppl_list)
        if temp_list[idx] == prev_num:
            idx += 1
        prev_idx = idx

    num = temp_list[idx]
    
    res_list.append(num)
    ppl_list.remove(num)
    prev_num = num
    
    
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