T = int(input())

arr = []


for _ in range(T):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort(key = lambda x: x[0])
dp = [0] * arr[T-1][0]


for i in range(T):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)