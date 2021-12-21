from collections import deque
import sys
que = deque()

T = int(input())

arr = []
for i in range(T):
    arr.append(sys.stdin.readline())

for i in range(len(arr)):
    arr[i] = arr[i].split()

for i in range(T):
    if arr[i][0] == 'push':
        que.append(arr[i][1])
    elif arr[i][0] == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(que))
    elif arr[i][0] == 'pop':
        if len(que)>0:
            print(que.popleft())
        else:
            print(-1)
    elif arr[i][0] == 'back':
        if len(que)>0:
            print(que[len(que)-1])
        else:
            print(-1)
    elif arr[i][0] == 'empty':
        if len(que) > 0:
            print(0)
        else:
            print(1)