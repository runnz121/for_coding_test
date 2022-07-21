from collections import deque

n = int(input())

arr = ['A']

que = deque(arr)

while n > 0:

    for _ in range(len(que)):

        x = que.popleft()

        if x == 'A':
            que.append('B')
        else:
            que.append('B')
            que.append('A')
    n -= 1

answer = [0,0]

for k in range(len(que)):
    if que[k] == 'A':
        answer[0] += 1
    else:
        answer[1] += 1

print(*answer)