# 전부 요격할 수 있는 요격 미사일 수의 최솟값 구하기!

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

# 일단 짧은 것부터 확인
# 겹치는 것 없는 애들 새롭게 표시하기
# ㄴㄴ

# <다른 방법>
# 끝나는 지점이 작은 걸로 배열
# 끝나는 지점 <= 시작 지점 일 때마다 추가
def solution(targets):
    answer = 1

    targets.sort(key=lambda x:(x[1],x[0]))
    
    misail_end = targets[0][1]
    for target in targets:
        if misail_end <= target[0]:
            answer += 1
            misail_end = target[1]    

    print(answer)
    return answer

solution(targets)