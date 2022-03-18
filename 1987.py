a, b = map(int, input().split())

arr = []

for i in range(a):
    res = list(map(str, input()))
    arr.append(res)

check = [[False] * b for _ in range(a)]

ans = []
cnt = 0

def dfs(x, y):

    if x > a or x < 0 or y > b or y < 0:
        return

    global ans
    global cnt

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(b):
        for j in range(i, a):

            if check[i][j]:
                continue

            check[i][j] = True
            if arr[i][j] not in ans:
                ans.append(arr[i][j])
                cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

            dfs(nx, ny)
            cnt -= 1
            ans.pop()
dfs(0, 0)

print(count)