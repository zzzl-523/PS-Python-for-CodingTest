from itertools import combinations

# 친구 정보 세팅
N, M = map(int, input().split())
friends_num_list = [[] for idx in range(N)]

for _ in range(M):
    num1, num2 = map(int, input().split())
    friends_num_list[num1-1].append(num2-1)
    friends_num_list[num2-1].append(num1-1)

num_min = 4000

for me_idx, friends_list in enumerate(friends_num_list):
    check0 = True

    # 각 경우에서 셋이 모두 친구인 경우 True 반환하기
    for j in range(len(friends_list)-1):    
        check1 = me_idx in friends_num_list[friends_list[j]]
        for k in range(j+1, len(friends_list)):
            check2 =  me_idx in friends_num_list[friends_list[k]]
            check3 = friends_list[j] in friends_num_list[friends_list[k]] and friends_list[k] in friends_num_list[friends_list[j]]
            
            check0 = check1 and check2 and check3

            # 셋이 모두 친구라면, 해당 경우의 전체 친구 수 구하기 - 서로
            if check0:       
                num = len(friends_list)+len(friends_num_list[friends_list[j]])+len(friends_num_list[friends_list[k]])
                num -= 2*3
                if num < num_min:
                    num_min = num    

if num_min == 4000:
    print(-1)
else: print(num_min)
