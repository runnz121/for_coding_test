from collections import deque

n = int(input())

que = deque(['0','1','2','3','4','5','6','7','8','9'])
total = 9
if n <= 9:
    print(que[n])
    exit(0)

while que:
    c = que.popleft()

    for i in range(0, 10):
        if int(c[-1]) <= i:
            break
        que.append(c + str(i))
        total += 1
        if total == n:
            print(que[-1]) # 큐에 마지막으로 들어간게 해당 원소
            exit(0)
print(-1)