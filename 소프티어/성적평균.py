import sys

input = sys.stdin.readline

N, K =  map(int, input().split())
arr = list(map(int, input().split()))

for i in range(K):
  a, b =  map(int, input().split())
  avg = sum(arr[a-1:b])/float(abs(b-a)+1)
  print("{:.2f}".format(avg))