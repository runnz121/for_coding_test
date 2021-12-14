city = int(input())
km = list(map(int, input().split()))
money = list(map(int, input().split()))

#선형탐색으로 하나씩 도시 넘길 때마다 최소값 지정
#최소값이면 다음 km 에서 곱하고 아니라면 최소값 변경후 곱함

cost = 0
money = money[:-1]

min_value = 1e9
for i in range(len(money)):
    # print(min_value)
    if money[i] < min_value:
        min_value = money[i]
    # print(km[i])
    cost += min_value * km[i]
    # cost = min(money[1:]) * sum(km[1:]) + start
print(cost)