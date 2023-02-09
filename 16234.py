from collections import deque

n, l, r = map(int, input().split())

graph = []

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    