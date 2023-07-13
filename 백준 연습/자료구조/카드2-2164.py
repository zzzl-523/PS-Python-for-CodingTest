from collections import deque

N = int(input())
cards_list = deque([n for n in range(1, N+1)])

cnt = 0
while len(cards_list) > 1:
    if cnt%2==0:
        # 맨 위에 카드 버리기
        cards_list.popleft()
    else: 
        # 그 다음 위에 카드 바닥에 깔기
        cards_list.append(cards_list[0])
        cards_list.popleft()
      
    cnt += 1

if len(cards_list) == 1:
    print(cards_list[0])