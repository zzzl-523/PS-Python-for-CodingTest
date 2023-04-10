import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    answer=0
    for word in babbling:
        if regex.match(word):
            answer+=1
    return answer
