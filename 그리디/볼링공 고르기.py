n, m = map(int, input().split())
result = 0
list = list(map(int, input().split()))
list.sort()

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] != list[j]:
            result += 1

print(result)