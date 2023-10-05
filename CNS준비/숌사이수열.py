# N개의 다른 숫자로 구성되어 있는 집합 X
# 길이 2N인 숌 사이 수열 S를 만들려고 함
# 1. X에 들어있는 모든 수는 숌 사이 수열 S에 정확히 두 번 등장해야 함
# 2. X에 등장하는 수가 i라면, S에서 두 번 등장하는 i사이에는 수가 i개 등장해야 한다

# 랜덤하게 해볼까 ..?

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 1. 두 번씩 등장
arr = arr+arr

# 2. i개
def dfs(arr, visited, index, result, answer, checked):
    result.append(arr[index])
    # print(result)
    
    if len(result) == len(arr):
        print("왜이래?")
        print(result)

        

        answer.append(result)
        # print("answer: ", answer)
        return 
    
    # print(arr[index], visited, sep='---')
    print(visited)
    for i in range(len(arr)):
        if not visited[i]:
            visited[index] = True
            temp_v = [num for num in visited]
            temp_r = [num for num in result]
            temp_c = [num for num in checked]

            # print(arr[i], len(result), checked[arr[i]],  result)
            if checked[arr[i]] == -1:
                checked[arr[i]] = len(result)
                dfs(arr, visited, i, result, answer, checked)
            
            else:
                if len(result) - checked[arr[i]] == arr[i] + 1:
                    # print(arr[i], i, checked[arr[i]],  result)
                    dfs(arr, visited, i, result, answer, checked)
                # else:
                #     continue
            # dfs(arr, visited, i, result, answer, checked)
            
            visited = temp_v
            result = temp_r
            checked = temp_c
            
    
    # print("이거: ", visited)
    
    return 

answer = []
check_arr = [False]*17

for i in range(N):
    result = []
    visited = [False]*len(arr)
    visited[i] = True
    checked = [-1]*17
    checked[arr[i]] = 0
    print(checked)
    print("이번엔 뭐냐면 ", i)
    dfs(arr, visited, i, result, answer, checked)

print(answer)
if len(answer):
    print(*sorted(answer)[0])
else:
    print(-1)
