# 8개의 톱니 가진 톱니바퀴 4개가 일렬로 놓여짐
# 톱니바퀴를 총 K번 회전시키려 함
# 시계방향, 반시계방향 있음
# 회전할 때 
#   같은 극 : 옆 톱니 회전 X
#   다른 극 : 옆 톱니 회전
# 서로 맞닿은 톱니의 극이 다르면 B는 A가 회전한 방향과 반대로 회전

# 톱니의 초기 상태, 회전시킨 방법 => 최종 톱니바퀴 상태 구해라
# 입력 : 시계방향 순서대로, 
#       N->0 S->1
#       회전 횟수 K번
#       회전시킨 방법 순서대로 (톱니 번호, 방향)
#           방향 1 -> 시계
#           방향 2 -> 반시계

from collections import deque
import sys
input = sys.stdin.readline

# 톱니 상태 입력받기
states = [deque(list(input())[:-1]) for _ in range(4)]
K = int(input())
rotate_list = deque([tuple(map(int, input().split())) for _ in range(K)])

# 회전시키면 Index=2가 움직이고, 맞닿은 쪽은 Index=-2가 움직인다
# 1번째 -> idx 2
# 2번째 -> idx -2
# rotate 함수 ..?

while rotate_list:
    num, dir = rotate_list.popleft()
    num -= 1
    check = [(False, 0)]*4

    check[num] = (True, dir)
    for i in range(4):
        index = (num+i)
        if index < 3 and index>i and states[index][1] and states[index][2] != states[(num+i+1)%4][-2]:
            print(states[index][2], states[(num+i+1)%4][-2])
            check[(num+i+1)%4] = (True, check[index][1]*(-1))
        index = (num-i)
        if index >= 0 and index<i and states[index][1] and states[index][-2] != states[(num-i-1)%4][2]:
            print(states[index][-2], states[(num-i-1)%4][2])
            check[(num-i-1)%4] = (True, check[index][1]*(-1))

    print("check 출력 : ", check)
    for i in range(4):
        if check[index][0] == True:
            states[index].rotate(check[index][1])
    
    print("-----------------")
    print(*states, sep='\n')
