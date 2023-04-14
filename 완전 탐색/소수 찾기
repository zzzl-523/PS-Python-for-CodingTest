import math
from itertools import permutations

def checkPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False   
    return True

def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        arr = list(set(permutations(numbers,i+1)))
        for j in range(len(arr)):
            num = int(''.join(arr[j]))
            if arr[j][0]!='0' and num!=1:
                if checkPrime(num):
                    # print(num)
                    answer += 1

    return answer