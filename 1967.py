import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# https://koosaga.com/14
#  루트에서 가장 거리가 먼 점이 지름 안에 없다는 게 모순

# 첫번째 루트 노드에서 가장 먼 노드를 구한다
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위의 첫번째 루트노드에서 가장 먼 노드를 시작점으로 여기서 더 먼 노드를 구한다
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))