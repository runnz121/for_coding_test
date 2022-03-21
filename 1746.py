import sys
input = sys.stdin.readline
x, y = map(int, input().split())

a = set()
b = set()

for _ in range(x):
    a.add(input().rstrip())

for _ in range(y):
    b.add(input().rstrip())

arr = sorted(list(a & b))
print(len(arr))

for i in arr:
    print(i)