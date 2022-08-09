from collections import deque

start, end = map(int, input().split())


que = deque()

que.append(start)

cnt = 0

check = [False for i in range(end + 1)]



def bfs():

    global cnt


    while que:
        x = que.popleft()

        lists = [2*x, x-1, x+1]

        if x == end:
            break

        if not check[x]:
            check[x] = True
            for i in lists:
                y = end
                y = min(abs(i-y), y)
            que.append(y)
            cnt += 1

bfs()
print(cnt)


