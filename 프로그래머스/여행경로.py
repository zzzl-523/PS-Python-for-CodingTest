tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

departure = []*len(tickets)
arrival = []*len(tickets)
for i in range(len(tickets)):
    departure[i] = tickets[i][0]
    arrival[i] = tickets[i][1]

start = departure.index('ICN')

answer = [start]

for _ in range(len(tickets)):
end = arrival[start]
answer.append(end)
