# 연속된 N일 동안의 매매가 알고 있음
# 하루에 최대 1만큼 구매할 수 있음
# 판매는 얼마든지 가능

# 구매 -> -
# 판매 -> +

# 하락장이면 구매 X

# 뒤에서부터 오면서 max_value보다 작으면 구매
# 새로운 max_value 나오면 이전 max로 팔고 반복

def solution(t):
    N = int(input())
    prices = list(map(int, input().split()))

    print('#'+str(t), end=' ')

    max_value = prices[-1]
    stock_cnt = 0
    ans = 0
    for i in range(N-2, -1, -1):
        if prices[i] > max_value:
            ans += max_value*stock_cnt # 이전 것들은 이전 max로 팔기
            stock_cnt = 0
            max_value = prices[i] # max 업데이트

        elif prices[i] < max_value:
            ans -= prices[i]
            stock_cnt += 1
    
    if stock_cnt>0:
        ans += max_value*stock_cnt
    
    print(ans)


T = int(input())
N = 0
prices = []
ans = 0
for t in range(1, T+1):
    solution(t)