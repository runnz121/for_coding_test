import copy

n = int(input())

dp = [[0] * n for _ in range(n)]

vector = []

# n * m = n * len(row)

for i in range(n):
    row = list(map(int, input().split()))
    vector.append(row)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if vector[i][1] == vector[j][0]:
            dp[j][i] = vector[i][0] * vector[i][1] * vector[j][1]


print(dp)
