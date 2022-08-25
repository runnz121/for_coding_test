a, b = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = arr1 + arr2
ans.sort()
print(*ans)