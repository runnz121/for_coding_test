import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)

k = int(input())
arr = []
check = [[0] * k for _ in range(k)]

for i in range(k):
    arr.append(list(map(int, input().split())))

for p in range(k):
    for i in range(k):
        for j in range(k):
            if arr[i][j] == 1 or (arr[i][p] == 1 and arr[p][j] == 1):
                arr[i][j] = 1

for i in arr:
    print(*i)