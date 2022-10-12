n = int(input())
arr = list(map(int, input().split()))

line = [0] * n

line[n-1] = 1

for i in range(1, n):
    if line[i] != 0:
