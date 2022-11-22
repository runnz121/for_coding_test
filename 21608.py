import sys

input = sys.stdin.readline

n = int(input())

for i in range(9):
    x = list(map(int, input().split()))
    cur = x[0]
    friends = x[1:]