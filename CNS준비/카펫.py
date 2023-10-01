# 프로그래머스
# 노란색, 갈색으로 이루어진 카펫
# 노랑, 갈색 개수는 기억하는데 전체 크기 모름
# 노랑이 중앙. 갈색 테두리!

# 전체 크기 구하기
# 가로 >= 세로
# 약수 구하기
# => 노랑이에서 구해서 사각형 만들고, 거기서 가로,세로2씩 커지면 됨

import math

brown = 24
yellow = 24

def solution(brown, yellow):
    arr = []
    garo, sero = 0, 0
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow%i==0:
            sero = i
            garo = yellow//i
            total = brown + yellow
            if total%(sero+2)==0 and total%(garo+2)==0:
                arr.append((i, yellow//i))
    
    sero = arr[-1][0] + 2
    garo = arr[-1][1] + 2
    answer = [garo, sero]
    
    print(answer)
    return(answer)
    
solution(brown, yellow)
    

