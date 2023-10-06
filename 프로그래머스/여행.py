test = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
test2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def find(tickets, arr, visited, prev, result):
    print(result)
    print(arr, visited, prev)
    for i in range(len(arr)):
        # 이전 도착지 == 지금 출발지
        if arr[i][0] == prev and (not visited[i]):
            print("이거: ", arr[i])
            result.append(arr[i])
            visited[i] = True
            prev = arr[i]
            find(tickets, arr, visited, prev, result)
    
    print("return이욤: ", result)
    return result
            

def solution(tickets):
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
        result = [arr[i]]
        answer.append(find(tickets, arr, visited, arr[i][1], result))
        
    answer.sort()
    # answer.sort(key=lambda x:(x[0], x[1]))
    # answer = answer[0]
    return answer[0]


print(solution(test))
print(solution(test2))