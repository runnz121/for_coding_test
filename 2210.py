from collections import deque

arr = []
ans = []

for i in range(5):
    arr.append(list(map(int, input().split())))

def bfs():

    dx = [-1,1,0,0,]
    dy = [0,0,-1,1]
