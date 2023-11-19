# 농장의 크기는 항상 홀수
# 수확은 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능

# 2구역으로 나눠서 경계선 정하기

def solution(t):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    mid = N//2
    st, end = mid, mid
    ans = arr[0][mid] # 첫 줄

    for i in range(1, N):
        if i<=(mid):
            n_st = st - 1
            n_end = end + 1
        else:
            n_st = st + 1
            n_end = end - 1

        if 0<=n_st and n_end<=N-1 and n_st<=n_end:
            ans += sum(arr[i][n_st:n_end+1])
            st, end = n_st, n_end

    print('#'+str(t), ans)

T = int(input())
for t in range(1, T+1):
    solution(t)