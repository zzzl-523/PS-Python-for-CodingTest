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
def dfs(arr, visited, index, result, answer):
    visited[index] = True
    result.append(arr[index])
    
    print(result)
    if len(result) == len(arr):
        answer.append(result)
        return 
    
    print(arr[index], visited, sep='---')
    for i in range(len(arr)):
        if not visited[i]:
            temp = [num for num in visited]
            dfs(arr, visited, i, result, answer)
            print("이후는?")
            visited = temp
    
    print("이거: ", visited)
    print("answer: ", answer)
    return 

answer = []

for i in range(len(arr)):
    result = []
    visited = [False]*len(arr)
    print("이번엔 뭐냐면 ", i)
    dfs(arr, visited, i, result, answer)

print(answer)
