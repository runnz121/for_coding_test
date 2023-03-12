n, m = map(int, input().split())

bucket = [i for i in range(1, n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    left = bucket[x-1]
    right = bucket[y-1]

    bucket[x-1] = right
    bucket[y-1] = left


print(*bucket)

# 2 1 3 4 5
# 2 1 4 3 5
# 3 1 4 2 5
# 3 1 4 2 5