import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
n, m = map(int, input().split())


# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

def find(parent, x):
    r = x
    while r != parent[r]:
        r = parent[r]
    while x != r:
        x, parent[x] = parent[x], r
    return r


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n + 1)]


for i in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        union(parent, b, c)
    elif a == 1:
        if find(parent, b) == find(parent, c):
            print("YES")
        else:
            print("NO")


