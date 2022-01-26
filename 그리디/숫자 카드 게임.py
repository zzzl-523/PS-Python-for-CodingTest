# n,m을 공백을 기준으로 입력받기
n, m = map(int,input().split())
min_list = []

for i in range(n):
    data = map(int, input().split())
    min_list.append(min(data))

result = max(min_list)
print(result)
