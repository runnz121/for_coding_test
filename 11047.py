coin, money = map(int, input().split())

coins = []

for i in range(coin):
    coins.append(int(input()))


count = 0
max_value = -1e9
for i in range(coin-1, -1, -1):
    if money / coins[i] >= 0:
        div = money // coins[i]
        money = money - div * coins[i]
        count += div
print(count)
