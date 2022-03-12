import sys
from itertools import combinations

input = sys.stdin.readline

x = int(input())

arr = []
compare = []

for i in range(x):
    res = input().rstrip()
    arr.append(set(res))
lists = list(combinations(arr,2))


print(arr)


count = 0
for i in range(x):
    for j in range(i+1, x):
        if len(arr[i]) == len(arr[j]):
        #count += 1


print(count)