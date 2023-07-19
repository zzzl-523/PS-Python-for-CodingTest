import sys
input = sys.stdin.readline

T = int(input())
lines = [input().split() for _ in range(T)]

# print(lines)

for line in lines:
    result = ''
    for word in line:
        word_list = list(word)
        word_list.reverse()      
        result += ''.join(word_list)+' '
    print(result)

