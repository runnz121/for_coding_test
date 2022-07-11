import sys

sys = sys.stdin.readline

n = int(input())
arr = []

ans = 0

db = dict()

for i in range(n):
    x = list(str(input()))
    temp = [1] * len(x)

    for y in range(len(x)):
        for z in range(y, len(x)):
            if x[y] == x[z]:
                temp[z] += 1
                temp[y] += 1
    arr.append(temp)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        start = 0
        while True:
            if start == len(arr[i]) - 1:
                ans += 1
                break

            if arr[i][start] != arr[j][start]:
                break

            start += 1

print(ans)
