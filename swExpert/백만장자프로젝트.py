# 연속된 N일 동안의 매매가 알고 있음
# 하루에 최대 1만큼 구매할 수 있음
# 판매는 얼마든지 가능

# 구매 -> -
# 판매 -> +

# 하락장이면 구매 X

def check_up_down(arr):
    num = arr[0]
    for i in range(1, len(arr)):
        if num < arr[i]:
            return "up"
    
    return "down"
    
def recursive(i, stock, total):
    global ans

    if i==N:
        ans = max(ans, total)
        return()

    if stock>0:
        if prices[i]>(-total/stock):
            # 판매
            recursive(i+1, 0, total+prices[i]*stock)
    
    # 팔기
    recursive(i+1, stock+1, total-prices[i])
    # 팔기 X
    recursive(i+1, stock, total)


def solution(t):
    print('#'+str(t), end=' ')

    # 하락장 체크
    check = check_up_down(prices)
    if check=="down":
        print(0)
        return()
    

    recursive(0, 0, 0)
    print(ans)

    
T = int(input())
N = 0
prices = []
ans = 0
for t in range(1, T+1):
    ans = 0
    N = int(input())
    prices = list(map(int, input().split()))
    solution(t)