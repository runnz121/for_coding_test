import math

n= int(input())

dp = []

ugly = [2,3,5]

for a in range(n):
    for b in range(n):
        for c in range(n):
            res = math.pow(ugly[0],a) * math.pow(ugly[1],b) * math.pow(ugly[2],c)
            dp.append(math.ceil(res))
            dp.sort()
print(dp[n-1])
