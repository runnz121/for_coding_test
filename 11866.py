from collections import deque

a, b = map(int, input().split())

arr = deque()
ans = '<'

for i in range(1, a+1):
    arr.append(i)

cnt = 0
while cnt < a:
    for i in range(b-1):
        arr.append(arr.popleft())
    if cnt != a - 1:
        ans += str(arr.popleft()) + ',' +' '
    else:
        ans += str(arr.popleft())
    if cnt == a-1:
        ans += '>'
    cnt += 1
print(ans)