city = int(input())
km = list(map(int, input().split()))
money = list(map(int, input().split()))

cost = 0
money = money[:-1]

start = km[0]
end = sum(km)
for i in range(start, end):
