from collections import deque

a, b = map(int, input().split())

check = [-1] * 100001

que = deque()

def bfs(n, k):

    que.append(n)
    check[n] = 0

    while que:
        x = que.popleft()

        if x == k:
            return

        if (x * 2 <= 100000) and (check[x * 2] == -1):
            # 가중치가 0임으로 우선순위가 가장 높게 잡힌다 -> 큐 맨 앞에 넣음
            que.appendleft(x * 2)
            check[x * 2] = check[x]#가중치가 0임으로 같게만 설정 (시간 0 초)

        if x > 0 and check[x - 1] == -1:
            que.append(x - 1)
            check[x - 1] = check[x] + 1 # 가중치가 1 존재(시간 1초)

        if x < 100000 and check[x + 1] == -1:
            que.append(x + 1)
            check[x + 1] = check[x] + 1


bfs(a, b)

print(check[b])

