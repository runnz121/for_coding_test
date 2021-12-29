a, b = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start, end = 1, max(arr)
ans = []
ans.append(0)

while start <= end:
    mid = (start + end) // 2
    total = 0
    res = 0
    for i in arr:
        res = i - mid
        if res > 0:
            total += res
    if total >= b:
        ans.append(mid)
        if total > b:
            start = mid + 1
        else:
            end = mid - 1
    elif total > b:
        start = mid + 1
    else:
        end = mid - 1
ans.sort()
min_value = int(1e9)
for i in ans:
    comp = sum(ans) - (len(ans) * i)
    if comp == min_value:
        answer = i
    elif comp < min_value:
        answer = i
#print(ans)
print(i)

### 반례
#
# 2 7
# 1 7