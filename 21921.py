import copy
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
days = list(map(int, input().split()))

arr = [0 for _ in range(n)]

arr[0] = days[0]
arr[1] = days[0] + days[1]
for i in range(2, n):
    arr[i] = days[i] + arr[i-1]

comp = copy.deepcopy(arr)
for i in range(x, n):
    comp[i] = arr[i] - arr[i - x]


if max(comp) == 0:
    print("SAD")
else:
    cnt = 0
    print(max(comp))
    maxs = max(comp)
    for i in comp:
        if i == maxs:
            cnt += 1
    print(cnt)
