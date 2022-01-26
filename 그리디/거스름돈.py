money = int(input())
cnt = 0

coin_types = [500, 100, 50, 10]
for coin in coin_types:
    cnt += money // coin
    money = money % coin

print(cnt)