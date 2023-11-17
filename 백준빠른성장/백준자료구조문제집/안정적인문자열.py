import sys
input = sys.stdin.readline

T = 0
arr = []
is_open = False

while True:
    T += 1
    ans = 0
    arr = input()
    s = []
    if '-' in arr:
        break
    for char in arr:
        if char=='{':
            s.append(char)
        elif char=='}':
            if len(s)==0:
                ans += 1
                s.append('{')
            else:
                s.pop()

    if len(s)>0:
        ans += len(s)/2
    
    print(str(T)+'.',int(ans))