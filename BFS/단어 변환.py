from collections import deque

def BFS(words, begin, target, visited):
    queue = deque(begin)
    cnt = 0
    
    while queue:
        word = queue.popleft()
        if word == target:
            break
            
        for i in range(len(words)):
            if not visited[i]:
                for j in range(len(word)):
                    if words[i][j] != word[j] and words[i][j:] == word[j:]:
                        visited[i] = True
                        queue.append(words[i])
                        cnt += 1
                        break
    return cnt
                    

def solution(begin, target, words):

    visited = [False for _ in range(len(words))]
    
    if target not in words:
        return 0
    
    answer = BFS(words, begin, target, visited)
    
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)