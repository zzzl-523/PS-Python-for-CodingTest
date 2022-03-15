N = int(input())
people = []

for i in range(N):
    data = input().split()
    age = int(data[0])
    name = data[1]
    people.append((age, name, i))   # 나이, 이름, 순서

people.sort(key=lambda x:(x[0], x[2]))

for p in people:
    print(str(p[0]) + " " + p[1])
