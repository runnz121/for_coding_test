from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
# 방문 배열 만들고
visited = [False] * (n+1)

#무 방향성 노드 연결
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(arr, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        for i in arr[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

def dfs(arr, v, visited):
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            dfs(arr, i, visited)

cnt = 0
# 방문한게 아니면 bfs 에 넣고 cnt+= 1 증가
for i in range(1, n+1):
    if not visited[i]:
        bfs(arr, i, visited)
        cnt += 1
print(cnt)