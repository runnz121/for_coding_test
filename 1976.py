import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [i for i in range(n + 1)]

def find(arr, x):
    if arr[x] != x:
        arr[x] = find(arr, arr[x])
    return arr[x]

def union(arr, x, y):
    a = find(arr, x)
    b = find(arr, y)

    if a < b:
        arr[b] = a
    else:
        arr[a] = b

for i in range(1, n + 1):
    city = list(map(int, input().split()))
    for k in range(n):
        if city[k] == 1:
            union(arr, i, k+1)

desti = list(map(int, input().split()))
for j in range(1, len(desti)):
    if arr[desti[j]] != arr[desti[j-1]]:
        print("NO")
        exit()
print("YES")
