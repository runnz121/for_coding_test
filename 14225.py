import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

def back(depth, end):
    global tmp
    global check
    global total

    if depth == end:
        total.append(sum(tmp))
        return

    for i in range(n):
        if not check[i]:
            tmp.append(arr[i])
            check[i] = True
            back(depth + 1, end)
            tmp.pop()
            check[i] = False

total = []
for i in range(2, n + 1):
    tmp = []
    check = [False] * n
    back(0, i)

arr = arr + total
result = list(set(arr))

maxx = max(result)

for i in range(1, maxx):
    if i != result[i-1]:
        print(i)
        exit(0)
print(max(result) + 1)