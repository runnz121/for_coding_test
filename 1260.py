import sys
from collections import deque
input = sys.stdin.readline

a, b, c, = map(int, input().split())

graph = [[]for i in range(a+1)]

visd = [False] * (a+1)
visb = [False] * (a+1)


for i in range(b):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#숫자 작은것부터 방문
for i in graph:
    i.sort()

def DFS(graph, v, visd):
    visd[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visd[i]:
            DFS(graph, i, visd)


def BFS(graph, start, visb):
    que = deque([start])
    visb[start] = True

    while que:
        v = que.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visb[i]:
                que.append(i)
                visb[i] = True


DFS(graph, c, visd)
print()
BFS(graph, c, visb)