import math
num = int(input())

count = [0] * 10

while num > 0:
    div = num % 10
    num = num // 10
    count[div] += 1

res = math.ceil((count[6] + count[9]) / 2)
count[6], count[9] = res, res
cnt = max(count)
print(cnt)