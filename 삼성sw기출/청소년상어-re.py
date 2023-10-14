# 청소년 상어 - BOJ 19236

# 방향 8가지
# 1. 상어의 이동
#   물고기가 있으면 이동 가능
#   해당 방향으로만 이동 가능.
#   이동 가능 칸 없으면 집으로 돌아가고 물고기 이동
# 2. 물고기의 이동
#   해당 방향에 물고기 있으면 자리 교체
#   상어 있거나 경계 벗어나면 반시계 회전

# 8가지 방향
# [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
# (물고기 번호, 방향)

direction = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
global result
result = 0

def shark_move(maps, fish_arr, shark, total):
    global result

    # 상어 움직임
    x, y = shark[0]
    fish = fish_arr[maps[x][y]] # 잡힌 물고기

    fish[0] = -1                # 물고기 잡힘 표시
    maps[x][y] = -1
    shark[1] = fish[2]          # 상어 방향 <- 물고기 방향

    print("====== 물고기 잡음 ======")
    print(*maps, sep='\n')

    fish_move(maps, fish_arr, shark)

    print("====== 물고기 이동 완료 ======")
    print(*maps, sep='\n')
    print("물고기 목록: ", *fish_arr)

    for idx in range(4):
        new_maps = [[] for _ in range(4)]
        new_fish_arr = [[] for _ in range(17)]

        nx = shark[0][0] + direction[shark[1]-1][0] + idx
        ny = shark[0][1] + direction[shark[1]-1][1] + idx

        if nx<0 or nx>=4 or ny<0 or ny>=4 or maps[nx][ny]==-1:
            continue

        for i in range(len(maps)):
            for j in range(len(maps[0])):
                new_maps[i].append(maps[i][j])

        for i in range(1, len(fish_arr)):
            new_fish = fish_arr[i]
            new_fish_arr[i] = [new_fish[0], new_fish[1], new_fish[2]]

        new_total = total + maps[nx][ny]
        if new_total > result:
            result = new_total

        print(new_total)
        print(result)

        shark_move(new_maps, new_fish_arr, [(nx, ny), shark[1]], new_total)


    return

def fish_move(maps, fish_arr, shark):
    for idx in range(1, len(fish_arr)+1):
        fish = fish_arr[idx]
        num, pos, dir = fish
        x, y = pos

        if num>0:

            for _ in range(8):
                nx = x + direction[dir - 1][0]
                ny = y + direction[dir - 1][1]

                if nx<0 or nx>=4 or ny<0 or ny>=4 or (nx, ny)==shark[0]:
                    dir = dir%8 + 1
                    continue

                # print("=======이동 전 -----------")
                # print(*maps, sep='\n')
                # print(fish)

                # 물고기 이동
                fish[2] = dir
                fish[1] = (nx, ny)
                fish_arr[maps[nx][ny]][1] = (x, y)

                # print((x,y), (nx,ny))
                # print(maps[x][y], maps[nx][ny])
                maps[x][y], maps[nx][ny] = maps[nx][ny], maps[x][y] # 그냥 숫자

                print("이동 후 ============", num)
                print(*maps, sep='\n')

                break


    return



maps = [[] for _ in range(4)]
fish_arr = [[] for _ in range(17)]

for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if j%2 == 0:
            # 번호만 입력
            maps[i].append(arr[j])
            # (번호, 위치, 방향)
            fish_arr[arr[j]] = [arr[j], (i, j//2), arr[j+1]]

print(*maps, sep='\n')
print(fish_arr)

# 상어 (위치, 방향)
shark = [(0,0), 0]

shark_move(maps, fish_arr, shark, maps[0][0])

print(result)
