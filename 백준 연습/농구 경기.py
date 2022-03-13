N = int(input())
alpha = [0]*26
stri = ''

for _ in range(N):
    name = input()
    alpha[ord(name[0])-97] += 1

for i in range(26):
    if alpha[i] >= 5:
        stri += chr(i+97)
        
if stri == '':
    print("PREDAJA")
else:
    print(stri)