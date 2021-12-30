import sys
input = sys.stdin.readline


# https://ca.ramel.be/46
line = int(input())
graph = []

for _ in range(line):
    graph.append(list(map(int, input().split())))

minus, zero, one = 0,0,0
def div(x,y,n):
    global minus, zero, one
    start = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != start:
                div(x, y, n//3)
                div(x, y+n//3, n//3)
                div(x, y+2*n//3, n//3)
                div(x + n//3, y, n//3)
                div(x + n//3, y + n//3, n//3)
                div(x + n//3, y + 2*n//3, n//3)
                div(x + 2 * n//3, y, n//3)
                div(x + 2 * n//3, y + n//3, n//3)
                div(x + 2 * n//3, y + 2 * n//3, n//3)
                return
    if start == -1:
        minus += 1
        return
    elif start == 0:
        zero += 1
        return
    else:
        one += 1
        return

div(0,0,line)
print(minus)
print(zero)
print(one)

