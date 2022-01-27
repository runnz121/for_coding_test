x, y = map(int, input().split())

# graph = [[] * y for _ in range(x)]

graph = []

for i in range(x):
    graph.append(list(map(int, input())))

sums = 0

# 길이
for i in range(1, min(x,y)):
    for a in range(x - i):
        for b in range(y - i):
            if graph[a][b] == graph[a+i][b] == graph[a][b+i] == graph[a+i][b+i]:
                sums = max(sums, (i+1)**2)
if sums == 0:
    print(1)
    exit()
print(sums)