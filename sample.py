INF = int(1e9)

#노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
#2차원 리스트를 만들고 모든값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

print(graph)

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1): # 거처가는 부분
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])
# 예를 들면 2 -> 3으로 가는 방법을 구할때 , 2 -> 3으로 바로 가는것이 빠른지 , 아니면, 2 ->1 ,1 -> 3  으로 거처가는것이 빠른지를 알아봄

#수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        #도달할 수 없는 경우, 무한(infinity)라고 출력
        if graph[a][b] == INF:
            print("infiinty", end = " ")
        #도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=" ")
print()