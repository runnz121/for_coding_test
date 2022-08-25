x = int(input())
n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append(a * b)

if sum(arr) == x:
    print("Yes")
else:
    print("No")

