x = int(input())
ressum = 0
ans = 0
for i in range(1, x+1):
    a = i
    while a > 0:
        res = a % 10
        a = a //10
        ressum += res
    if ressum + i == x:
        ans = i
        break
    elif ressum > x:
        ans = 0
        break
    else:
        ressum = 0
        continue
print(ans)

