import sys
input = sys.stdin.readline

arr = [1, 1]

def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(2):
    N = int(input())
    nums = map(int, input().split())
    for num in nums:
        arr[i] *= num

result = str(GCD(arr[0], arr[1]))

if len(result)>=9:
    print(result[-9:])
else: print(result)