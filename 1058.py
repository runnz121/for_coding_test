n = int(input())

graph = []
ans = 0

for i in range(n):
    graph.append(list(map(str, input())))

check = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                check[i][j] = 1 # 서로 아는 친구가 있으면 1로 초기화

for x in check:
    ans = max(ans, sum(x))
print(ans)