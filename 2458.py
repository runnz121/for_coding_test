n, m = map(int, input().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

answer = 0

# 전체 6명인 학급에서 내가 3번째 로 키가 크다면
# 내 앞에는 2명이 있고, 내뒤에는 3명이 있다.
# 즉 나보다 큰 학생수는 나에 도달 할 수 있는 노드의 갯수와 같다

for i in range(1, n + 1):
    know_number = 0
    for j in range(1, n + 1):
        # 특정 노드가 다른 노드를 가르키는 횟수 + 다른 노드가 특정 노드를 가르키는 횟수 == n - 1(전체 학생 수 - 1(자기자신)) 이면 그 특정 노드의 순서를 알 수 있다.
        know_number += graph[i][j] + graph[j][i]
    if know_number == (n - 1):
        answer += 1

print(answer)