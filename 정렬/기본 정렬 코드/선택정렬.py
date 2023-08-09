# 자기보다 앞에 정렬을 (큰것부터) 돌면서 자기보다 큰 값이 나오면 그 앞 값과 swap

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]:
			array[j-1], array[j] = array[j], array[j-1] # 서로 바꿔준다
		else:
			break

print(array)