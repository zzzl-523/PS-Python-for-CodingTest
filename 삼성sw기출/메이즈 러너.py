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

N, M, K = tuple(map(int, input().split()))
# 미로 입력
board = [
    [0]*(N+1)
    for _ in range(N+1)
]
for i in range(1, N+1):
    board[i] = [0] + list(map(int, input().split()))

new_board = [
    [0]*(N+1)
    for _ in range(N+1)
]


# 여행객 입력
travelers = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(M)
]

# 출구 입력
exit = tuple(map(int, input().split()))

ans = 0
sx, sy, square_size = 0, 0, 0

# 여행객 이동
def move_travelers():
    global ans, exit
    for i in range(1, M+1):
        # 탈출
        if travelers[i] == exit:
            continue

        tx, ty = travelers[i]
        ex, ey = exit

        # 행이 다른 경우 행을 이동시켜봅니다.
        if tx != ex:
            nx, ny = tx, ty

            if ex > nx:
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not board[nx][ny]:
                travelers[i] = (nx, ny)
                ans += 1
                continue

        # 열이 다른 경우 열을 이동시켜봅니다.
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 열을 이동시킵니다.
            if not board[nx][ny]:
                travelers[i] = (nx, ny)
                ans += 1
                continue


# 가장 작은 정사각형 찾기
def find_minimum_square():
    global sx, sy, square_size
    # 한 명 이상의 참가자, 출구를 포함해야 함

    ex, ey = exit
    # 참가자 확인
    for sz in range(2, N):
        for x1 in range(1, N-sz+2):
            for y1 in range(1, N-sz+2):
                x2, y2 = x1+sz-1, y1+sz-1

                if not (x1 <= ex <= x2 and y1 <= ey <= y2):
                    continue

                is_traveler_in = False
                for i in range(1, M+1):
                    tx, ty = travelers[i]

                    if x1<=tx and tx<=x2 and y1<=ty and ty<=y2:
                        if not (tx==ex and ty==ey):
                            is_traveler_in = True

                    if is_traveler_in:
                        sx = x1
                        sy = y1
                        square_size = sz

                        return


# 미로 회전
def rotate_square():
    # 해당 부분의 벽 -1
    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            if board[x][y]:
                board[x][y] -= 1

    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            ox, oy = x-sx, y-sy
            rx, ry = oy, square_size-ox-1
            new_board[sx+rx][sy+ry] = board[x][y]

    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            board[x][y] = new_board[x][y]

def rotate_travlers_and_exit():
    global exit

    # 여행자 회전
    for i in range(1, M+1):
        tx, ty = travelers[i]

        if sx<=tx and tx<sx+square_size and sy<=ty and ty<sy+square_size:
            ox, oy = tx-sx, ty-sy
            rx, ry = oy, square_size-ox-1
            travelers[i] = (sx+rx, sy+ry)

    # 출구 회전
    ex, ey = exit

    if sx<=ex and ex<sx+square_size and sy<=ey and ey<sy+square_size:
        ox, oy = ex-sx, ey-sy
        rx, ry = oy, square_size-ox-1
        exit = (sx+rx, sy+ry)


for cnt in range(K):
    move_travelers()

    is_all_exited = True
    for i in range(1, M+1):
        if travelers[i] != exit:
            is_all_exited = False

    if is_all_exited:
        break

    find_minimum_square()
    rotate_square()
    rotate_travlers_and_exit()

print(ans)
print(*exit, sep=' ')






