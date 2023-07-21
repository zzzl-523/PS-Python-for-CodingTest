from itertools import combinations_with_replacement

nums = [1, 5, 10, 50]
N = int(input())

num_list = []

for num in combinations_with_replacement(nums, N):
    if sum(list(num)) in num_list:
        continue
    else:
        num_list.append(sum(list(num)))

print(len(num_list))