# DP
def solution(triangle):
    answer = 0
    
    DP = [thing for thing in triangle]
    
    for i in range(1, len(triangle)):
        DP[i][0] += DP[i-1][0]
        for j in range(1, len(triangle[i])-1):
            DP[i][j] = max(DP[i][j]+DP[i-1][j-1], DP[i][j]+DP[i-1][j])
        DP[i][-1] += DP[i-1][-1]
    
    answer = max(DP[-1])
    
    return answer