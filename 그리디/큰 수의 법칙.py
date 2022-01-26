n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 2가지 뿐
data.sort(reverse=True) # 내림차순 정렬
first = data[0] # 가장 큰 수
second = data[1] # 두 번째로 큰 수

# 가장 큰 수가 나온 횟수
cnt = k*int((m/(k+1))) + m%(k+1)

result = cnt*first + (m-cnt)*second
print(result)
