pos = input()
x = int(pos[1])
y = int(ord(pos[0])) - int(ord('a')) + 1

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

cnt = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    
    cnt += 1

print(cnt)