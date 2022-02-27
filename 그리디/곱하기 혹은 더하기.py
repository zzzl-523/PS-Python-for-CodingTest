str = input()
list = []
for c in str:
    list.append(int(c))

result = list[0]

for n in list:
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)
