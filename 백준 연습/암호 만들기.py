import collections
import itertools 

L, C = map(int, input().split())
data = input().split()
data.sort()
stri = []
answer = ''
v_cnt = 0
cnt = 0

for i in itertools.combinations(data, L):
    stri = list(i)
    answer = ''
    v_cnt = 0
    cnt = 0
    for j in range(L):
        if stri[j] in "aeiou":
            v_cnt += 1
        else:
            cnt += 1
        answer += stri[j]
    if v_cnt>=1 and cnt>=2:
        print(answer)
