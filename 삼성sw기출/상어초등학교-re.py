# 골드5
# |r1 - r2| + |c1 - c2| = 1을 만족 => 상하좌우
# 1. 좋아하는 학생 4명 중 최대로 배치
# 2. 비어있는 칸이 가장 많은 칸으로 자리 정함
# 3. 행 번호 최소 -> 열 번호 최소

# 종료 후 만족도 구하기
# 만족도: 0, 1, 10, 100, 1000


def first_condition(info, infos, visited):
    num, friends = info[0], info[1]
    dxy = [(0,1), (0,-1), (1,0), (-1,0)]

    # for move in dxy:

def second_condition(info, infos, visited):
    return
    


def func(info, infos, visited, N):
    num, friends = info[0], info[1]
    dxy = [(-1,0), (1,0), (0,-1), (0,1)]

    # 전체 돌면서 상하좌우에 아무도 없기/친구 있기 조사
    check = [-1]*4 # 상하좌우

    for i in range(N):
        for j in range(N):
            for idx, move in enumerate(dxy):
                if visited[i][j]==-1: # not visited
                    nx = i + move[0]
                    ny = j + move[1]

                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue

                    if visited[nx][ny]==-1:
                        check[idx] = 0 # 아무도 없음
                    else:
                        check[idx] = visited[nx][ny]

            print(check)
            # print(*visited, sep="\n")
            if check[0]==0 and check[1]==0 and check[2]==0 and check[3]==0:
                # 아무도 없다는 뜻
                second_condition(info, infos, visited)
            # else:
                # 친구 있다는 뜻
                # first_condition()



                    



    first_condition(info, infos, visited)



import sys
input = sys.stdin.readline

N = int(input())
infos = [[0]]*(N*N+1)
visited = [[-1]*(N) for _ in range(N)]
# print(*visited, sep='\n')

for i in range(1, N*N+1):
    value = list(map(int, input().split()))
    infos[i] = [value[0], value[1:]]
    
    func(infos[i], infos, visited, N)

print(*infos, sep='\n')

