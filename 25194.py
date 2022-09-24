n = int(input())
days = list(map(int, input().split()))

check = [False] * n

arr = []

ends = 1

for i in range(1, n + 1):
    ends *= i

def back(depth, end):

    global arr

    if sum(arr)%4 == 0 and arr:
        print("YES")
        exit()

    if depth == n:
        return

    if end == ends:
        print("NO")
        exit()

    for i in range(n):
        if check[i]:
            continue

        check[i] = True
        arr.append(days[i])
        back(depth + 1, end + 1)
        check[i] = False
        arr.pop()

back(0, 0)