from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))

print(result)
