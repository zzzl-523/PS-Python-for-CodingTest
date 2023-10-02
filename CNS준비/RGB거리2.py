import sys
input = sys.stdin.readline

N = int(input())
RGB_list = []
for i in range(N):
    RGB_list.append(list(map(int, input().split())))
    # for j in range(3):
        # RGB_list[i].append(((j, arr[j])))

# print(RGB_list)

total = 0

def DFS(RGB_list, index, prev_color, total, N, init_color, result):
    
    # print(index)
    
    
    # print(RGB_list[index])
    new_total = total + RGB_list[index][prev_color]
    # print("total: ", new_total)

    if index==N-1:
        result.append(new_total)
        return result

    if index==N-2:
        for i in range(3):
            if i != prev_color and init_color!=i:
                DFS(RGB_list, index+1, i, new_total, N, init_color, result)
        
    else:
        for i in range(3):
            if i != prev_color:
                DFS(RGB_list, index+1, i, new_total, N, init_color, result)
            
    return result

result = []
for i in range(3):
    if i==0:
        result = DFS(RGB_list, 0, i, total, N, i, result)
        # print("결과 한번: ", result)
    else: result = min(result, DFS(RGB_list, 0, i, total, N, i, result))

print(min(result))