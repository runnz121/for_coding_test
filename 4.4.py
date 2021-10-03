n,m = map(int, input().split())
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

