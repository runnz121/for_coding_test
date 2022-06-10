n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
check = [False] * n

result = []
ans = []


def permutation(n, m, l):
    global ans

    if l == m:
        print(*result)
        ans.append(result)
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            result.append(int(arr[i]))
            permutation(n, m, l + 1)
            result.pop()
            check[i] = False

permutation(n, m, 0)

print(ans)
# ans.sort()
# for i in ans:
#     print(i)
