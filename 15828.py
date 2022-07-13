from collections import deque

buffer = int(input())

temp = deque()
while True:
    x = int(input())
    if x == -1:
        break
    if x == 0:
        temp.popleft()
    else:
        if buffer > len(temp):
            temp.append(x)
        else:
            continue

if len(temp) == 0:
    print('empty')
else:
    print(*temp)