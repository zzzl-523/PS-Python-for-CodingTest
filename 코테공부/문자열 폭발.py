# 문자열 폭발
# 골드4
# 스택

# re 써보기
import re
import sys
input = sys.stdin.readline

text = input().strip()
bomb = input().strip()

print(text, bomb)
arr = re.split('C4', text)
print(re.split('C4', text))
