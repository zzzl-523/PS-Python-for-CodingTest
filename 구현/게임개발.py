sero, garo = map(int, input().split())
visited = [[0]*garo for _ in range(sero)]

x, y, direction = map(int, input().split())
visited[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(sero):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1: direction = 3

cnt = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        # 뒤로 가기
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        turn_time = 0

print(cnt)
