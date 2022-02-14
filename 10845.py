from collections import deque
import sys

input = sys.stdin.readline

cnt = int(input())
que = deque()

for i in range(cnt):
    arr = list(map(str, input().split()))
    if arr[0] == 'push':
        que.append(arr[1])
    elif arr[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            res = que.popleft()
            print(res)
            que.appendleft(res)
    elif arr[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            bacs = que.pop()
            print(bacs)
            que.append(bacs)
    elif arr[0] == 'size':
        print(len(que))
    elif arr[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
