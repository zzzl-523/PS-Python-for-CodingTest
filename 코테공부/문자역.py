# 문자열 폭발
# 골드4
# 스택

# re 써보기
import re
import sys
input = sys.stdin.readline

text = input().strip()
bomb = input().strip()

while True:
    if bomb not in text:
        break
    arr = re.split(bomb, text)
    text = ''.join(arr)

if text:
    print(text)
else:
    print("FRULA")
