import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()
que.append(1)

ans = [0] * (n + 1)

# 현재 방문 노드와 연결되어 있는 값들을 확인
# 해당 값이 체크 배열에서 0인 경우 그 노드의 값을 현재 노드값으로 바꿔줌
# 현재 노드 값이 해당 원소값의 부모배열이 되는 거임
def bfs():
    while que:
        now = que.popleft()
        for nx in graph[now]:
            if ans[nx] == 0:
                ans[nx] = now
                que.append(nx)
print(graph)

bfs()
print(ans)
res = ans[2:]
for x in res:
    print(x)
#https://d-cron.tistory.com/22

# dfs 의 경우 무조건 부모노드인 1부터 시작 ->
# 1부터 자식노드로 향하기 때문에 해당 노드에 있는 원소값들에
# 부모노드값을 넣어주면 자동적으로 자식 노드가 형셩됨
visited = [0] * (n+1)
def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)
dfs(1)