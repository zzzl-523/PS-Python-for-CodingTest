# 누가 선물 많이 받을지
# 선물 주고받은 기록 있으면 -> 이번 달까지 더 많이 준 사람이 다음 달에 하나 받음
# 기록 없거나 수 같음 -> 선물지수
    # 선물 지수 = 준 - 받은
    # A, B중에서 다음 달에 B가 받음
    # 선물지수도 같으면 다음달에 선물 주고받지 X

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

def solution(friends, gifts):
    N = len(friends)
    answer = [0]*N
    board = [[0 for _ in range(N)] for _ in range(N)]

    friends_list = {}
    gift_score = [0]*N
    for i in range(N):
        friends_list[friends[i]] = i
    
    for i in range(len(gifts)):
        arr = gifts[i].split()
        giver = friends_list[arr[0]]
        receiver = friends_list[arr[1]]
        
        board[giver][receiver] += 1
        gift_score[giver] += 1
        gift_score[receiver] -= 1
    
    # print(*board, sep='\n')

    for i in range(N):
        for j in range(i+1, N):
            if board[i][j]>0 and (board[i][j] != board[j][i]):
                if board[i][j] > board[j][i]:
                    answer[i] += 1
                elif board[i][j] < board[j][i]:
                    answer[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    answer[i] += 1
                elif gift_score[i] < gift_score[j]:
                    answer[j] += 1
    
    print(answer)


    return answer

solution(friends, gifts)