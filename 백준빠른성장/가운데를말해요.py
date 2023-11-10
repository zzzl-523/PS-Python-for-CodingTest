# 단기간 성장
# 홀수면 전체 수 중에서 중간값
# 짝수면 중간 두 수 중에서 작은 수

N = int(input())

arr = [-1]

for i in range(1, N+1):
    arr.append(int(input()))

    # 짝수
    if i%2==0:
        print(min(arr[len(arr)//2], arr[(len(arr)//2)+1]))
    else:
        print(sorted(arr)[len(arr)//2])

# sort 방법 바꿔보기!  