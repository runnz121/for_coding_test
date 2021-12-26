import sys
input = sys.stdin.readline
#노드의 갯수
n = int(input())
#간선의 갯수
m = int(input())
INF = int(1e9)

graph = [[INF] *(n+1) for _ in range(n+1)]

#자기자신 출발 도착 노드 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#해당값 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    #가장 짧은 간선 정보만 저장하기 위해 부등호 처리
    if c < graph[a][b]:
        graph[a][b] = c

#점화식
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end= ' ')
        else:
            print(graph[a][b], end= ' ')
    print()