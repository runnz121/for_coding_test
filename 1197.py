n, m = map(int, input().split())

parent = [0] * (n + 1)
edges = []
result = 0

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)