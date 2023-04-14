import numpy as np

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tmp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = tmp
    
    sizes_t = np.array(sizes).transpose()
    
    max_w = int(max(sizes_t[0]))
    max_h = int(max(sizes_t[1]))
    answer = max_w * max_h
    
    return answer