def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0]*(N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    oper, x, y = map(int, input().split())

    if oper == 0:
        union_parent(parent, x, y)
    elif oper == 1:
        if find_parent(parent, x) == find_parent(parent, y):
            print('YES')
        else:
            print('NO')