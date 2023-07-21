# rotate
# 왼쪽으로 가서 -되면 해당 idx값 그대로 -로 사용
# 오른쪽 끝으로 가서 넘어가면 해당 idx값%N 값으로 사용
# 이미 터진 다음에는 0으로 바꿔주기 (0은 없으니까)

import sys
input = sys.stdin.readline

def check(num_list, index, is_positive):
    if index > len(num_list)-1:
        index %= len(num_list)
    elif index < 0:
        index += len(num_list)

    if num_list[index] == 0:
        if is_positive:
            return check(num_list, index+1, is_positive)
        else:
            return check(num_list, index-1, is_positive)
    else:
        return index
        

N = int(input())
num_list = list(map(int, input().split()))

now_idx = 0
result = [1]

for _ in range(N-1):
    moved = now_idx + num_list[now_idx]

    num_list[now_idx] = 0
    moved = check(num_list, moved, num_list[now_idx]>0)
    
    now_idx = moved

    result.append(moved + 1)
    # num_list.remove(num_list[moved])
    # now_idx -= 1

print(str(result).replace(',','').replace('[','').replace(']',''))