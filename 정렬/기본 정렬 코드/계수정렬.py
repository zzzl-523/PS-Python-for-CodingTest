array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]*(max(array)+1)

for num in array:
	count[num] += 1

for idx, cnt in enumerate(count):
	for _ in range(cnt):
		print(idx, end=' ')