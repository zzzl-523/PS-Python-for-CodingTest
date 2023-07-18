import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home_list = sorted([int(input()) for _ in range(N)])

l = 1
r = home_list[-1] - home_list[0]

def binary_search(a, l, r, C, result):
    mid = (l+r)//2
    count = 1
    prev_num = a[0]
    if l <= r:
        for idx in range(1, len(a)):
            if a[idx] >= prev_num + mid:
                prev_num = a[idx] 
                count += 1
                if count >= C:
                    break

        if count < C:
                binary_search(a, l, mid-1, C, result)
        else:
            result = max(result, mid)
            binary_search(a, mid+1, r, C, result)
    else:
        print(result)
        return

binary_search(home_list, l, r, C, l)

# 도현이의 집 N개가 수직선 위에 있음
# 각 집의 좌표는 X_1~X_N
# 언제 어디서나 와이파이 즐기기 위해 C개의 공유기 설치 예정
# 한 집에는 공유기 하나만
# 가장 인접한 두 공유기 사이 거리 가능한 크게
# => C개의 공유기를 N개의 집에 적당히 설치, 가장 인접한 공유기 사이 거리 최대로
# 각 공유기 사이는 하나 이상의 빈 칸 존재!

# 구해야 할 것을 mid로 두면 된다! => 가장 인접한 두 공유기 사이의 최대 거리
# (1 + (최대-최소))//2=mid
# 1 2 4 8 9
# mid = 1 + 8 // 2 = 4
# 4
# 1+4
# 2+4
# 4+4 -> 8 
# 길이-(idx(8)+1) >=(N-2) ==> 뒤로는 가장 가까운 idx 차이가 4보다 커야함