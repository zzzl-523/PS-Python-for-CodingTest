# DFS ..


# for문 계속..10000개
# 10000*10000 ..?
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def DFS(this, tickets, route, visited):
    departure = this[0]
    arrival = this[1]
    print("루트 ", route)

    if len(route) == len(tickets)+1:
        return route


    for idx, ticket in enumerate(tickets):     
        if ticket[0] == arrival and not visited[idx]:
            print(this, ticket)
            visited[idx] = True
            route = DFS(ticket, tickets, route+[ticket[1]], visited)
    
    print("뭐야?: ", route)
    return route


def solution(tickets):
    answer = []

    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            route = ["ICN", ticket[1]]
            visited = [False]*len(tickets)
            visited[idx] = True
            # result = []
            answer.append(DFS(ticket, tickets, route, visited))
            # print("--------------", ticket)
    
    answer.sort()
    print(answer[0])
    # print(answer[0])
    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])==["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]) == ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]) == ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]) == ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]) == ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]) == ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]) == ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"])
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]]) == ["ICN", "AOO", "ICN", "AOO", "COO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]) == ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]) == ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])