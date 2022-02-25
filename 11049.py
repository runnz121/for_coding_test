n = int(input())

dp = [0] * (n+1)

dp[0] = 0
dp[1] = 0
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

print(dp)
# 갯수
for i in range(2, n+1):

    for x in range(0, n+1):
        for y in range(x, n+1):
            print(arr[x])
            # if arr[x][1] == arr[y][0]:
            #     dp[i] = min(arr[x][0]*arr[x][1]*arr[y][1] , dp[i])

print(dp)