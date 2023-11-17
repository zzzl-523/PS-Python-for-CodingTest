import sys
input = sys.stdin.readline

T = 0
arr = []
is_ok = False
while True:
    T += 1
    arr = input()
    for char in arr:
        if is_ok and char=='{':
            