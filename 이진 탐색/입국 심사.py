import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time_list = sorted([int(input()) for _ in range(N)])

l = 0
r = time_list[0]*M

def binary_search(a, l, r, M, result):
    mid = (l+r)//2

    if l<=r:
        total_people = 0
        for time in a:
            total_people += mid//time
        
        if total_people < M:
            binary_search(a, mid+1, r, M, result)
        else:
            result = min(result, mid)
            binary_search(a, l, mid-1, M, result)
    
    else:
        print(result)

binary_search(time_list, l, r, M, r)

# 여행을 떠난다
# 상근이 포함 총 M명
# 입국 심사대는 총 N개
# K번 심사대에 앉아있는 심사관이 한 명을 심사하는 데 드는 시간 T_K
# 비어있으면 가도 되지만, 더 빠른 심사대를 기다렸다가 거기서 받아도 된다
# => 기다리는 시간도 시간으로 포함해도 된다. 그러면 (0+최소 시간*인원 수)//2 = 8로 잡고 시작해도 되겠다

# 예제를 생각해보자.
# 7~10 mid는 7*6 = 42 -> 21
# 21//7 = 3
# 21//10 = 2
# => 5

# 22~42 => 64//2 = 32
# 32//7 = 4
# 32//10 = 3
# => 7

# 22~31 => 53//2 = 26
# 26//7 = 3
# 26//10 = 2
# => 5

# 27~31 => 58//2 = 29
# 29//7 = 4
# 29//10 = 2
# => 6

# 27~28 => 55//2 = 27
# 27//7 = 3
# 27//10 = 2
# => 5

# 28~28 => 56//2 = 28
# 28//7 = 4
# 28//10 = 2
# => 6