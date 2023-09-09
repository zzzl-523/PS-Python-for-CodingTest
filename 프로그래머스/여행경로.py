# 주어진 항공권 모두 사용이 함정!!!
# 실패 케이스도 고려해야함!

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

tickets.sort(key=lambda x: (x[0], x[1]))

departures = []
arrivals = []

for ticket in tickets:
    departures.append(ticket[0])
    arrivals.append(ticket[1])

end = "ICN"
answer = [end]

for _ in range(len(tickets)):
    start_idx = departures.index(end)
    departures.remove(end)

    end = arrivals[start_idx]
    arrivals.remove(end)
    
    answer.append(end)

print(answer)
