# 수식
# 0~9, +,-,x
# 괄호 안에는 연산자 하나만!
# 중첩된 괄호는 금지
# 결과의 최댓값 구하는 프로그램 작성해라

import sys
input = sys.stdin.readline

N = int(input())
sik = list(input().rstrip())

answer = -123456789

def check(sik, idx):
    global answer

    if idx >= len(sik)-1:
        # print(sik)
        result = int(sik[0])
        for i in range(1,len(sik)-1):
            if sik[i]=='+':
                result+=int(sik[i+1])
            elif sik[i]=='-':
                result-=int(sik[i+1])
            elif sik[i]=='*':
                result*=int(sik[i+1])
        
        answer = max(answer, result)
        return 

    # 괄호 X
    check(sik, idx+2)

    # 괄호 O
    new_sik = sik[:idx]+[str(eval(''.join(sik[idx:idx+3])))]+sik[idx+3:]
    check(new_sik, idx+2)

check(sik, 0)
print(answer)