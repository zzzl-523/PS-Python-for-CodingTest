import re
global regex 
def check(compare):
    global regex
    if regex.match(compare):
        return False
    return True
    
def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        # 시간초과 주의!
        # regex = re.compile('^'+phone_book[idx])     
        # if regex.match(phone_book[idx+1]):
        #     return False
        
        if phone_book[idx+1][:len(phone_book[idx])] == phone_book[idx]:
            return False
         
    return answer