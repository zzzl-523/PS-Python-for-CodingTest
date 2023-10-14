# 코드 트리

# 미로 탈출 게임
# 미로 구성
# 1. (1,1)로 시작
# 2. 미로의 상태
#   1) 빈 칸
#   2) 벽
#       - 내구도 가짐 1~9
#       - 회전할 때, 내구도 1씩 깎임
#       - 내구도 0==빈 칸
#   3) 출구

# 조건
# 최단거리
# 모든 참가자는 동시에 움직임
# 상하 이동 우선

# 미로 회전
# 가장 작은 정사각형
# 정사각형 시계방향 회전 90도. 회전된 벽은 내구도 1씩 깎임

N, M, K = map(int, input().split())
maps = [[11 for _ in range(N+1)]]
members = []
global exit
exit = []

# maps 입력받기
for _ in range(N):
    maps.append([11] + list(map(int, input().split())))
# members 입력받기
for i in range(M, 0, -1):
    x, y = arr = list(map(int, input().split()))
    members.append(arr)
    maps[x][y] = -1*i

# exit 입력받기
x, y = arr = list(map(int, input().split()))
exit = arr
maps[x][y] = 100


print(*maps, sep='\n')

def check_short(now, next, exit):
    now_short = abs(now[0] - exit[0]) + abs(now[1] - exit[1])
    next_short = abs(next[0] - exit[0]) + abs(next[1] - exit[1])

    if now_short < next_short:
        return False
    else:
        return True
def check_dist(now, exit):
    return abs(now[0] - exit[0]) + abs(now[1] - exit[1])

def rotate_box(box_start, num, maps, members):
    global exit
    temp = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            temp[i][j] = maps[box_start[0]+num-1-j][box_start[1]+i]

    for i in range(num):
        for j in range(num):
            if 0 < temp[i][j] < 10:
                maps[box_start[0] + i][box_start[1] + j] = temp[i][j] -1
            else:
                if temp[i][j] < 0:
                    members[temp[i][j]] = [box_start[0] + i, box_start[1] + j]
                elif temp[i][j] == 100:
                    exit = [box_start[0] + i, box_start[1] + j]
                maps[box_start[0] + i][box_start[1] + j] = temp[i][j]

    print("---------exit, members 확인------")
    print(exit, members)

# 1 2 3
# 4 5 6
# 7 8 9
#
# 7 4 1
# 8 5 2
# 9 6 3
#
# [3,1] [2,1] [1,1]
# [3,2] [2,2] [1,2]
# [3,3] [2,3] [1,3]


d_xy = [(0,-1), (0,1), (-1,0), (1,0)]

result = 0

for cnt in range(K):
    # print("@@@@@@@@@@", cnt+1,"회차입니당", "@@@@@@@@@@@")
    shortest_pos = [-1, -1]
    shortest_dist = check_dist((1, 1), (N, N))
    # BFS로 다 돌려보기
    for idx, member in enumerate(members):
        print("member 보여줍시다", member)
        is_remove = False
        x, y = member

        if (x,y)!=(-1,-1):
            move_list = []
            for i in range(4):
                nx = x + d_xy[i][0]
                ny = y + d_xy[i][1]

                if nx<1 or nx>N or ny<1 or ny>N or 10>maps[nx][ny]>0:
                    continue
                if maps[nx][ny]==100:
                    maps[x][y] = 0
                    result += 1

                    members[idx] = [-1, -1]
                    # print(members[idx])
                    # print("제거!", members)

                    is_remove = True
                    break

                check = check_short((x,y),(nx, ny),exit)
                if check:
                    move_list.append([nx, ny])

            if not is_remove:
                if len(move_list)>0:
                    # print("move_list: ", move_list)
                    members[idx] = list(move_list[-1])
                    # print(member)
                    maps[members[idx][0]][members[idx][1]] = maps[x][y]
                    maps[x][y] = 0


                    # print(exit)

                    result += 1

                if check_dist(members[idx], exit) < shortest_dist:
                    shortest_pos = members[idx]
                    shortest_dist = check_dist(members[idx], exit)

            # print(member)
            # print(shortests)
    print("이동 후 확인")
    print(*maps, sep='\n')

    # 이동 끝나면 회전
    target = shortest_pos
    # print(shortest_pos)

    # 정사각형 만들기
    num = max(abs(target[0]-exit[0])+1, abs(target[1]-exit[1])+1) # 정사각형 한 변
    # 실제 변의 길이는 num+1, 더할 때는 index+num
    arr = []
    for i in range(1, N):
        for j in range(1, N):
            sero, garo  = i+num, j+num
            if garo <= N+1 and sero <= N+1:
                # print("exit 때문에? ", exit, target, garo, sero, (i, j, num))
                # print(i<=target[0]<sero, i<=exit[0]<sero, j<=target[1]<garo, j<=exit[1]<garo)
                if i<=target[0]<sero and i<=exit[0]<sero and j<=target[1]<garo and j<=exit[1]<garo:
                    # print("여길 못 들어가?")
                    arr.append((i, j))
                    break
    arr.sort(key=lambda x:(x[0],x[1]))
    box_start = arr[0]
    print(num, box_start)
    #
    print("확인해보자 ==================", cnt+1)
    print(*maps, sep='\n')
    print("----")
    rotate_box(box_start, num, maps, members)
    # print(*maps, sep='\n')



print(result)
print(*exit, sep=' ')










