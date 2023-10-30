# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수(UNION 연산 수행 횟수) 입력 받기
v, e = map(int, input().split())
parent = [0]*(v+1)

# 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# UNION 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
for i in range(1, v+1):
    print(parent[i], end=' ')

print()