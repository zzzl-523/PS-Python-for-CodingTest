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

direction = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

def shark_move(num, dir):
    return

def fish_move(maps, fish_arr):
    # 물고기 수 만큼
    for fish in fish_arr:
        # 물고기 잡아 먹히면 -1
        if fish[0]>0:
            num, pos, dir = fish
            x, y = pos
            print(num, pos, dir)
            while True:
                nx = x + direction[dir-1][0]
                ny = y + direction[dir-1][1]

                if nx<0 or nx>=4 or ny<0 or ny>=4 or maps[nx][ny][0]<0:
                    # 가능한 게 없으면 회전
                    dir = (dir+1)%9
                    continue

                # 가능하면 교체
                print(maps[nx][ny])
                new_num = maps[nx][ny][0]
                maps[x][y], maps[nx][ny] = maps[nx][ny], maps[x][y]

                # 위치만 업데이트
                fish_arr[num-1][1] = (nx, ny)
                fish_arr[new_num-1][1] = (x,y)

                print(*maps, sep='\n')
                print(fish_arr)

                break

    return


maps = []
fish_arr = [[] for _ in range(16)]

for i in range(4):
    input_arr = list(map(int, input().split()))
    arr = []
    for j in range(len(input_arr)):
        if j%2==0:
            num = input_arr[j]
            dir = input_arr[j+1]
            # (물고기 번호, 방향)
            arr.append([num, dir])
            # fish_arr (물고기 번호, 현재 위치, 방향)
            fish_arr[num-1] = [num, (i, j//2), dir]

    maps.append(arr)

print(*maps, sep='\n')
print(fish_arr)

# 상어의 위치
x, y = 0, 0
fish = maps[x][y]
num = fish[0]
fish_arr[num-1][0] = -1
maps[x][y][0] = -1

fish_move(maps, fish_arr)

print(*maps, sep='\n')


