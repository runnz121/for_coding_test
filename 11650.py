import sys

T = int(input())

arr = []

for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  arr.append((a,b))

arr = sorted(arr, key = lambda x: (x[0], x[1]))

for i in arr:
  print(str(i[0])+' '+str(i[1]))