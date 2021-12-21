from collections import deque
import sys

T = int(input())

arr = deque()
ans = deque()
for _ in range(T):
    arr.append(sys.stdin.readline()[:-1])

for i in range(T):
    arr[i] = arr[i].split()


for i in range(T):
    if arr[i][0] == 'push_front':
        ans.appendleft(arr[i][1])

    if arr[i][0] == 'push_back':
        ans.append(arr[i][1])

    if arr[i][0] == 'pop_front':
        if len(ans) > 0:
            print(ans.popleft())
        else:
            print(-1)

    if arr[i][0] == 'pop_back':
        if len(ans) > 0:
            print(ans.pop())
        else:
            print(-1)

    if arr[i][0] == 'size':
        print(len(ans))

    if arr[i][0] == 'empty':
        if len(ans) == 0:
            print(1)
        else:
            print(0)

    if arr[i][0] == 'front':
        if len(ans) > 0:
            print(ans[0])
        else:
            print(-1)

    if arr[i][0] == 'back':
        if len(ans) > 0:
            print(ans[len(ans)-1])
        else:
            print(-1)