N = int(input())
list = []
for i in range(N):
    list.append(input().split())

list.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in list:
    print(student[0])