# 주사위 n개
# 주사위에 쓰인 수의 구성은 모두 다름
# A, B n/2개씩 가져감
# 각각 주사위 모두 굴리고, 나온 수를 모두 합해서 점수 계산하기
# 점수가 더 큰 쪽이 승리, 같으면 무승부
# A가 자신이 승리할 확률이 가장 높아지도록 주사위 가져가려 함 => 이거 구하기

from itertools import combinations
from collections import Counter

A_sum = {}
B_sum = {}
dice_arr = []
ans = 0
def recursiveA(comb, idx, total, sum_arr):
    global A_sum
    if len(comb)==idx:
        if total not in sum_arr:
            sum_arr[total] = 1
        else: sum_arr[total] += 1
        # print(sum_arr)
        # A_sum = sum_arr
        A_sum = sum_arr
        
        # print(total)
        return sum_arr

    for i in range(6):
        recursiveA(comb, idx+1, total + comb[idx][i], sum_arr)
    
def recursiveB(comb, idx, total, sum_arr):
    global ans, B_sum

    # print(comb)
    if len(comb) == idx:
        if total not in sum_arr:
            sum_arr[total] = 1
        else: sum_arr[total] += 1

        B_sum = sum_arr
        # for key, value in A_sum.items():
        #     # print(key,value)
        
        #     if total < key:
        #         # A_sum.pop()
        #         ans += value
        return sum_arr

    # if total > A_sum[-1]:
    #     return

    for i in range(6):
        recursiveB(comb, idx+1, total + comb[idx][i], sum_arr)
    

def solution(dice):
    global dice_arr, A_sum, ans, B_sum
    dice_arr = dice
    answer = 0
    result = []
    
    comb1 = list(combinations(range(len(dice)), int(len(dice)/2)))

    # print(comb1)
    for comb in comb1:
        A_sum = 0
        ans = 0
        arr = []
        arrB = []
        for i in range(len(dice)):
            if i in comb:
                arr.append(dice[i])
            else:
                arrB.append(dice[i])

        # print(arr, arrB)
        recursiveA(arr, 0, 0, {})
        
        # print(A_sum)
        recursiveB(arrB, 0, 0, {})
        
        # print(A_sum)
        # print(B_sum)

        for keyA, valA in A_sum.items():
            for keyB, valB in B_sum.items():
                if keyA>keyB:
                    ans += valA*valB
        
        if answer < ans:
            result = comb
            answer = ans
        # print(ans)
    
    ans_arr = []
    for i in range(len(result)):
        ans_arr.append(result[i]+1)

    return ans_arr


solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])