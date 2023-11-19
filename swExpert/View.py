# 양쪽 모두 거리 2 이상 공간 확보

def solution(t):
    ans = 0
    N = int(input())
    bs = list(map(int, input().split()))

    for i in range(0+2, N-2):
        # 왼쪽, 오른쪽 체크
        if bs[i-1] < bs[i] and bs[i-2] < bs[i] and bs[i+1] < bs[i] and bs[i+2] < bs[i]:
            ans += min(bs[i] - max(bs[i-1], bs[i-2]), bs[i] - max(bs[i+1], bs[i+2]))

    print("#"+str(t), ans)

T = 10
for t in range(1, T+1):
    solution(t)