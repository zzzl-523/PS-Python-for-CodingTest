# 출력 형식 정확하게!
T = int(input())

answer = []
for test_case in range(1, T + 1):
    cnt = 0
    arr = list(map(int, input().split()))
    # print(list(arr))
    for j in range(len(arr)):
    	if arr[j]%2==1:
        	cnt += arr[j]
    
    answer.append(cnt)

for idx, ans in enumerate(answer):
    print('#'+str(idx+1)+' '+str(ans))
