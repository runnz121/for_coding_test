n, m = map(int, input().split())


graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

min_dis = 0

chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])

check = [False] * len(chicken)

