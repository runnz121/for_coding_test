import sys

T = int(input())
arr = []
for _ in range(T):
    strings = str(sys.stdin.readline()[:-1])
    lens = len(strings)
    arr.append((strings,lens))

arr = sorted(set(arr),key = lambda x : (x[1],x[0]))

for i in range(len(arr)):
    print(arr[i][0])