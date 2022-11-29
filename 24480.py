import sys
sys.setrecursionlimit(300000)

n, m, r = map(int, input().split())

arr = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

check = [0] * (n + 1)
check[r] = 1

for i in arr:
    i.sort(reverse=True)

ans = []

cnt = 1
def dfs(v):
    global cnt

    for i in arr[v]:
        if check[i]:
            continue
        cnt += 1
        check[i] = cnt
        dfs(i)
dfs(r)

for x in range(1, n+1):
    print(check[x])