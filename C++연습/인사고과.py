# 완탐으로 할까? 했는데 길이가 100,000이면.. 
# 두 번 돌면 100000*100000 -> 터진다

scores = [[2,1],[1,4],[3,2],[3,2],[2,2]]	

def solution(scores):
    
    me = sum(scores[0])
    scores.sort(key=lambda x:(-x[0],x[1]))
    
    answer = []
    
    prev = scores[0]
    for i in range(1, len(scores)):
        is_incentive = True
        
        if scores[i][1] < prev[1]:
            is_incentive = False
        
        if is_incentive:
            answer.append(sum(scores[i]))
    
    answer.sort(reverse=True)

    for i in range(len(answer)):
        if answer[i] == me:
            print(i+1)
            return i+1
        if answer[i]<me:
            break

    return -1
    

    # return answer

solution(scores)