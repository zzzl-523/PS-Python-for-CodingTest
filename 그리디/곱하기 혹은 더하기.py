str = input()
list = []
for c in str:
    list.append(int(c))

result = list[0]

for i in range(1, len(list)):
    if list[i] <= 1 or result <= 1:
        result += list[i]
    else:
        result *= list[i]

print(result)
