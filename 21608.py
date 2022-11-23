import sys
from collection import deque
input = sys.stdin.readline

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
check = [[False for _ in range(n)] for _ in range(n)]

for i in range(n * n):
    x = list(map(int, input().split()))
    cur = x[0]
    friends = x[1:]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈칸 갯수를 dict에 저장
def count_empty():

    db = dict()

    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                