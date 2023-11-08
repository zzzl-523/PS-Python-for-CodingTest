# 백트래킹
# 배열 만들면서 바로 뒤에 이어지는지 나쁜수열 확인
# 좋은수열일 경우, 저장.

# 확인할 때는 같은 숫자 연속 안 되도록 생성 / 만들면서 확인

import copy
N = int(input())
ans = 10*81

def check(arr):
    for i in range(2,(len(arr)//2)+1):
        if arr[len(arr) - i:] == arr[len(arr) - i*2 :  len(arr) - i ]:
            return False
    
    return True
        

def dfs(arr, num):
    global ans

    if not check(arr):
        return
    if len(arr)==N:
        ans = min(ans, int(''.join(arr)))
    
    if num == 1:
        dfs(copy.deepcopy(arr)+[2], 2)
        dfs(copy.deepcopy(arr)+[3], 3)
    elif num == 2:
        dfs(copy.deepcopy(arr)+[1], 1)
        dfs(copy.deepcopy(arr)+[3], 3)
    elif num == 3:
        dfs(copy.deepcopy(arr)+[2], 2)
        dfs(copy.deepcopy(arr)+[1], 1)

 
for i in range(3):
    dfs([i], i)

print(ans)
