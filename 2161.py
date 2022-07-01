from collections import deque

n = int(input())

ans = []
arr = [i for i in range(1, n+1)]

q = deque(arr)

while len(q) > 1:
    x = q.popleft()
    ans.append(x)
    a = q.popleft()
    q.append(a)

ans.append(q[0])

print(*ans)