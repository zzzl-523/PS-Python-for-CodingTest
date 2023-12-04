# 문자열 폭발
# 골드4
# 스택

import sys
input = sys.stdin.readline

text = input().strip()
bomb = input().strip()

st = []
for i in range(len(text)):
    st.append(text[i])
    if ''.join(st[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            st.pop()

if len(st)>0:
    print(''.join(st))
else:
    print("FRULA")