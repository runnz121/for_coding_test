<<<<<<< HEAD
import sys
input = sys.stdin.readline

# https://castlerain.tistory.com/100
n, m = map(int, input().split())

graph = []

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

sum_data = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + graph[i-1][j-1]


for k in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])
=======
n, m = map(int, input().split())

arr = []

for i in range(n):
>>>>>>> 616309a1b4c657ffee215aff4ac4dc451f427773
