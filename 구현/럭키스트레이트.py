score = input()
mid = len(score)/2 - 1
left = 0
right = 0
result = "READY"

for i in range(len(score)):
    if i <= mid:
        left += int(score[i])
    else:
        right += int(score[i])

if left == right:
    result = "LUCKY"

print(result)