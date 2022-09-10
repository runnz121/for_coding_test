n, m = map(int, input().split())

graph = []

for i in range(n):
    arr = list(map(int, input()))

    arr = arr[::-1]

    graph.append(arr)

for i in graph:
    init = ''
    for j in i:
        init += str(j)
    print(init)