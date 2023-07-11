def cal(n, k):
    cnt = 0
    if n <= 3:
        return 1
        
    if n%2==0:
        cnt += cal(n/2, k)
    else:
        a1 = k+(n-k)/2
        a2 = (n-k)/2

        if a1!=a2:
            cnt += cal(a1, k)
            cnt += cal(a2, k)
    return cnt

    
def solution(n, k):
    answer = cal(n, k)
    print(answer)

solution(7,3)


        