def solution(s):
    answer = 0
    
    length = [len(s)]
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:step]
        cnt = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1
                
            
        if cnt > 1:
            compressed += str(cnt) + prev
        else:
            compressed += prev

        length.append(len(compressed))
    
    length.sort()
    answer = length[0]
    return answer