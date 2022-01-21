#sum() 합
result = sum([1, 2, 3, 4, 5])
print(result)

#min() 최솟값
result = min(7, 3, 5, 2)
print(result)

#max() 최댓값
result = max(7, 3, 5, 2)
print(result)

#eval() 해당 수식을 계산한 결과
result = eval("(3+5)*7")
print(result)

#sorted() 정렬된 결과 반환
result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

#sort() 객체의 값을 바로 변경
data = [9, 1, 8, 5, 4]
data.sort()
print(data)

#lambda로 두 번째 원소를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)
