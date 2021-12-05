import math

n = int(input())
while n > 0:
    H, W, N = map(int, input().split())

    room = math.ceil(N/H)
    level = N - (H * (room-1))
    if level < 0:
        level = N - H
    n -=1
    print(level*100+room)