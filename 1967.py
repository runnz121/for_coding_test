n = int(input())

tree = [[] for i in range(n + 1)]
node = []

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    node.append(a)

setNode = set(node)
total = 0

visited = [False] * (n + 1)

def dfs(start):

    visited[start] = True


