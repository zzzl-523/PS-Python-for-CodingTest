str = input()
cnt = [0, 0]
cnt[int(str[0])] += 1

for i in range(1, len(str)):
    if str[i] != str[i-1]:
        cnt[int(str[i])] += 1

result = min(cnt[0], cnt[1])
print(result)