import sys

T = int(input())
arr = list(sys.stdin.readline().split())
arr.sort(reverse=True, key = lambda x: x[0])

print(arr)