def DFS(idx, value, numbers, target):
    cnt = 0
    N = len(numbers)
    
    if idx == N:
        if value == target:
            return 1
        else: return 0
    
    cnt += DFS(idx+1, value+numbers[idx], numbers, target)
    cnt += DFS(idx+1, value-numbers[idx], numbers, target)
    
    return cnt
    
def solution(numbers, target):
    answer = DFS(0, 0, numbers, target)
    
    return answer