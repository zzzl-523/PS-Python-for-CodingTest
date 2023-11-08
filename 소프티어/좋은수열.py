# 백트래킹
# 배열 만들면서 바로 뒤에 이어지는지 나쁜수열 확인
# 좋은수열일 경우, 저장.

# 확인할 때는 같은 숫자 연속 안 되도록 생성 / 만들면서 확인

import copy
N = int(input())
# ans = 10**81

def check(arr):
    for i in range(1,(len(arr)//2)+1):
        if arr[len(arr) - i:] == arr[len(arr) - i*2 :  len(arr) - i ]:
            return False
    
    return True
        

def dfs(num):
    # global ans

    if len(num)==N:
        # ans = min(ans, int(num))
        # print(ans)
        print(num)
        exit()
    
    for i in '123':
        if check(num+str(i)):
            dfs(num+str(i))

 
dfs('1')