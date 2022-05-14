a, b = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

arr1 = set(x) - set(y)
arr2 = set(y) - set(x)

print(len(arr1) + len(arr2))