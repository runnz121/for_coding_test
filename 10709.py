x, y = map(int, input().split())
arr = []

for k in range(x):
    arr.append(list(str(input())))

ans = [[-1]*y for _ in range(x)]


for x in range(len(arr)):
    for w in range(len(arr[x])):
        if arr[x][w] == 'c':
            # if ans[x][w-1] != 0:
            #     ans[x][w] = ans[x][w-1] + 1
            # else:
            ans[x][w] = 0
        elif ans[x][w-1] != -1:
            ans[x][w] = ans[x][w-1] + 1


for k in ans:
    print(*k)