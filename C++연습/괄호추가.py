# 수식
# 0~9, +,-,x
# 괄호 안에는 연산자 하나만!
# 중첩된 괄호는 금지
# 결과의 최댓값 구하는 프로그램 작성해라

import sys
input = sys.stdin.readline

N = int(input())
sik = input()
# 괄호 안에는 숫자 2개, 연산자 1개만 가능

total = 0

is_plus = False
is_minus = False
is_multiple = False
is_gwalho = False

def command(command):
    global is_plus, is_minus, is_multiple, is_gwalho

    if command == '+':
        is_plus = True
    elif command == '-':
        is_minus = True
    elif command == '*':
        is_multiple = True
    elif command == '(':
        is_gwalho = True
    elif command == ')':
        is_gwalho = False

def calculate(num, sik_num):
    print(sik_num)
    if sik_num ==' \n':
        return
        
    if is_plus:
        num += int(sik_num)
    if is_minus:
        num -= int(sik_num)
    if is_multiple:
        num *= int(sik_num)
    return num


def calculator(sik):
    result = 0

    gwalho_num = 0
    
    for i in range(len(sik)):
        if sik[i]=='+' or sik[i]=='-' or sik[i]=='*' or sik[i]=='(' or sik[i]==')':
            command(sik[i])
            if sik[i]==')':
                result = calculate(result, gwalho_num)
            continue

        if is_gwalho:
            gwalho_num = calculate(gwalho_num,sik[i])
        else:
            result = calculate(result,sik[i])

    return result
            
        

# 일단 걍 다 돌려보기
def check(siksik, idx, total):
    new_sik = siksik
    arr1 = new_sik[:idx-1]
    arr2 = new_sik[idx+2:]
    arr = '('+new_sik[idx-1:idx+2]+')'

    # print("출력 확인: ", arr1, arr, arr2)
    if len(arr)< 3+2 and len(arr2)<3:
        total = calculator(siksik)
        return total
        
    
    # 괄호 X
    check(siksik, (idx+2), total)

    # 괄호 O
    check(arr1+arr+arr2, (idx+4)+2, total)


answer = check(sik, 1, total)
print(answer)