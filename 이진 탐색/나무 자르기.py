import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))
tree_heights = sorted(tree_heights)

def binary_search(a, l, r, M):
    mid = (l+r)//2

    if l<=r:
        sum_ = 0
        for tree in a:
            if tree>mid:
                sum_ += tree-mid

        if sum_ < M:
            binary_search(a, l, mid-1, M)
        elif sum_ >= M:
            binary_search(a, mid+1, r, M)
    else:
        print(mid)
        return mid

result_height = binary_search(tree_heights, 0, max(tree_heights), M)