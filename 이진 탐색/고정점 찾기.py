def binary_search(a, l, r):
    if l > r:
        return -1
    mid = (l+r) // 2

    if a[mid] == mid:
        return a[mid]
    elif a[mid] > mid:
        return binary_search(a, l, mid - 1)
    else:
        return binary_search(a, mid+1, r)
    

N = int(input())
array = list(map(int, input().split()))

answer = binary_search(array, 0, N-1)
print(answer)