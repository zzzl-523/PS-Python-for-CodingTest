import sys
input = sys.stdin.readline

nums = int(input())
score = [0]

for i in range(nums):
    score.append(int(input()))


DP = [0]*(nums+1)
DP[1] = score[1]
DP[2] = max(score[1]+score[2], score[2])
DP[3] = max(score[1]+score[3], score[2] + score[3])

for i in range(4, nums+1):
    DP[i] = max(DP[i-3] + score[i-1] + score[i] , DP[i-2] + score[i])

print(DP[nums])