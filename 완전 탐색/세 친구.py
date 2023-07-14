from itertools import combinations

N, M = map(int, input().split())
friends_num_list = [tuple([idx, []]) for idx in range(N)]

for _ in range(M):
    num1, num2 = map(int, input().split())
    friends_num_list[num1-1][1].append(num2-1)
    friends_num_list[num2-1][1].append(num1-1)

comb_list = list(combinations(friends_num_list, 3))
num_min = 4000

print(comb_list)
for list_ in comb_list:
    for idx in range(3):
        zero = 0
        plus1 = (idx+1)%3
        plus2 = (idx+2)%3

        print(list_[plus1][0], list_[zero][1])
        check1 = list_[plus1][0] in list_[zero][1]
        check2 = list_[plus2][0] in list_[zero][1] 
        if check1 and check2:
            print(list_)
            num = len(list_[zero][1])
            if check1:
                num -= 1
            if check2:
                num -= 1
            
            if num < num_min:
                num_min = num

if num_min == 4000:
    print(-1)
else: print(num_min)
