#리스트에 포함된 원소를 하나씩 확인하며 remove_set에 포함되어 있지 않았을 때만 result에 넣는 코드
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} #5를 한 번만 넣어도 모든 5가 지워짐

result = [i for i in a if i not in remove_set]
print(result)