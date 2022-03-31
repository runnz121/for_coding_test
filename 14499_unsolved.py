N, M, x, y, commands_num = map(int, input().split())

graph = []
for i in range(N):
    ntos, wtoe = map(int, input().split())
    graph.append((ntos, wtoe))

command = list(map(int, input().split()))

