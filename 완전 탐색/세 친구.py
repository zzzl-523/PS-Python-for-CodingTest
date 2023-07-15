from itertools import combinations
import sys

input = sys.stdin.readline

# 친구 정보 세팅
N, M = map(int, input().split())
friends_num_list = [[] for _ in range(N)]

for _ in range(M):
    num1, num2 = map(int, input().split())
    friends_num_list[num1-1].append(num2-1)
    friends_num_list[num2-1].append(num1-1)

num_min = 4000

for friends_list in friends_num_list:
    # 셋이 모두 친구인 경우 찾기
    for j in friends_list:    
        for k in friends_num_list[j]:
            if k in friends_list:
                # 셋이 모두 친구라면, 해당 경우의 전체 친구 수 구하기 - 서로
                num = len(friends_list)+len(friends_num_list[j])+len(friends_num_list[k])
                num -= 2*3
                if num < num_min:
                    num_min = num    
            
            
if num_min == 4000:
    print(-1)
else: print(num_min)
