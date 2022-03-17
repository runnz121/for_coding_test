while True:
    full = list(map(int, input().split()))
    arr = full[1:]
    if len(full) == 1:
        if full[0] == 0:
            break
    arr.sort()
    check = [False] * len(arr)
    ans = []
    def comb(depth, start):

        global ans

        if depth == 6:
            print(*ans)
            return

        for i in range(start, len(arr)):
            if check[i]:
                continue

            check[i] = True
            ans.append(arr[i])
            comb(depth + 1, i)
            ans.pop()
            check[i] = False
    comb(0,0)
    print()