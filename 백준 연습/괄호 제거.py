from itertools import combinations

in_ = input()

st_1 = []
list_ = []

for idx, ex in enumerate(in_):
    if ex == '(':
        st_1.append(idx)
    elif ex == ')':
        list_.append([st_1.pop(), idx])

res = []
for i in range(len(list_)):
    comb_list = list(combinations(list_, i+1))

    
    for j in range(len(comb_list)):
        tmp_in_ = list(in_)
        for k in range(i+1):
            # string은 요소를 바꿀 수 없으므로 list로 변환     
            tmp_in_[comb_list[j][k][0]] = '_'
            tmp_in_[comb_list[j][k][1]] = '_'
    
            
        # list를 다시 string으로 변환하기 위해 Join 사용
        tmp_in_ = ''.join( s for s in tmp_in_)
        tmp_in_ = tmp_in_.replace('_', '')
        res.append(tmp_in_)

# 중복 제거
prev_result = ''
for result in sorted(res):
    if prev_result != result:
        print(result)
    prev_result = result
    