stri = input()
result = []
value = 0
for n in stri:
    if n.isalpha():
        result.append(n)
    else:
        value += int(n)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
