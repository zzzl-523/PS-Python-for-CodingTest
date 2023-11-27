# 정점 번호, 도넛, 막대, 8자

dic = {}
new_v = {}
def dfs(root):
    global dic, new_v

    if new_v[root] >= 3:
        return

    if root not in new_v:
        new_v[root] = 1
    else:
        new_v[root] += 1
    
    for i in range(len(dic[root])):
        dfs(dic[root][i])
    


def solution(edges):
    global dic
    answer = []
    
    point = 0
    donut = 0
    stick = 0
    eight = 0   

    visited = {}
    visited[edges[0][0]] = 0

    for i in range(len(edges)):
        if edges[i][0] not in dic:
            dic[edges[i][0]] = [edges[i][1]]
        else:
            dic[edges[i][0]].append(edges[i][1])
        
        if edges[i][1] not in visited:
            visited[edges[i][1]] = 1
        else:
            visited[edges[i][1]] += 1
    
    print(visited)
    total = 0
    for key, val in visited.items():
        if val==0:
            point = key
            total = len(dic[point])
            for num in dic[key]:
                visited[num] -= 1
            break

    for key, val in visited.items():
        if val==2:
            eight += 1
        elif val==3:
            eight += 1
    
    stick = total -(donut-eight)
   
    print([point, donut, stick, eight])
    
    for i in range(len(dic[point])):
        dfs(dic[point][i])
    print(new_v)

    
    
    # for key, val in dic.items():
        # if len(val)>=2:
        #     dfs(key, val)

    #         eight += 1
    
    # print(visited)
    
    # print(eight)


    # dfs(edges[0])

    return answer

solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])