N = int(input())
data = list(map(int, input().split()))

data.sort()
print(data[(N-1)//2])