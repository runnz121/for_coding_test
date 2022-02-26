import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

edge = []

distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((a,b,c))

print(edge)

def bell(start):
    distance[start] = 0

    for i in range(v): # 노드 갯수
        for j in range(e): # 간선갯수
            currnet = edge[j][0]
            next = edge[j][1]
            cost = edge[j][2]

            if distance[currnet] != INF and distance[next] > distance[currnet] + cost: