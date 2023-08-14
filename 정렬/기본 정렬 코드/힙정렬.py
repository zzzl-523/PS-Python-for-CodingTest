# Heap
# 기본 라이브러리는 min heap 기준
# 시간복잡도는 O(logN). N개에 적용한다면 O(NlogN)

import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        print(h)
        result.append(heapq.heappop(h))

    return result

result = heapsort([0, 3, 6, 2, 7, 8, 4, 9, 1, 5])
print(result)