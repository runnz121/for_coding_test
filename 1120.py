a, b = map(str, input().split())

count = 0
if len(a) == len(b):
    for i in range(len(b)):
        if a[i] != b[i]:
            count += 1
else:
    for i in range(0, len(b)-len(a)+1):
        maxx = 0
        for j in range(len(a)):
            # print(b[i:i+len(a)])
            if a[j] == b[i:i+len(a)][j]:
                maxx += 1
            count = max(maxx, count)
    count = len(a) - count
print(count)