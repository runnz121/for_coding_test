n = int(input())
arr = [i for i in range(1, n + 1)]
visit = [False] * n
ans = []

def back(depth, start):

    global ans

    if depth == n:
        print(*ans)
        return

    for i in range(n):
        if visit[i]:
            continue

        visit[i] = True
        ans.append(arr[i])
        back(depth + 1, i)
        ans.pop()
        visit[i] = False

back(0, 0)
