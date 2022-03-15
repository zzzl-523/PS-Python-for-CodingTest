import math

N, M = map(int, input().split())
bosuk = [0]*M

for i in range(M):
    bosuk[i] = int(input())

bosuk.sort()    # 보석 오름차순 정렬
rest = N - M    # 못 받은 학생 수
student = []

for i in range(M-rest):
    student.append(bosuk[i])

for i in range(M-rest, N):
    for j in range(M-rest, M):
        student.append(math.ceil(bosuk[j]/2))
        student.append(math.floor(bosuk[j]/2))

student.sort(reverse=True)
print(student[0])

