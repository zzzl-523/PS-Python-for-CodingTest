n = int(input())
people = list(map(int, input().split()))
cnt = 0
group_cnt = 0

for p in people:
    cnt += 1
    if cnt >= p:
        cnt = 0
        group_cnt += 1

print(group_cnt)