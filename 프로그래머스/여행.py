def find(time, arr, visited, prev, result):
    global answer
    nomore = True
    if len(result)==len(arr)+1:
        if not answer:
            answer = result
        else:
            temp = [answer, result]
            temp.sort()
            answer = temp[0]

    for i in range(len(arr)):
        # 이전 도착지 == 지금 출발지
        
        if arr[i][0] == prev and (not visited[i]):
            nomore = False
            new_visited = [thing for thing in visited]
            new_visited[i] = True
            find(time, arr, new_visited, arr[i][1], result+[arr[i][1]])   

def solution(tickets):
    global answer
    answer = []
    arr = []
    cnt = 0
    
    # ICN을 맨 앞에 배치    
    for i in range(len(tickets)):
        ticket = tickets[i]
        if tickets[i][0]=="ICN":
            arr.insert(0, ticket)
            cnt += 1
        else:
            arr.append(ticket)
    
    for i in range(cnt):      
        visited = [False]*len(arr)
        visited[i] = True
        result = arr[i]
        find(i+1, arr, visited, arr[i][1], result)
    
    # answer.sort()
    # answer = answer[0]
    return answer
