T = int(input())
arr = []
for _ in range(T):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort(key = lambda x: x[0])
dp = [0] * arr[T-1][0]

print(arr)

# LIS(가장 긴 수열 일반 공식)
for i in range(T):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j] # 더 큰 숫자로 바뀌고 1이 더해짐
            #print(j,i,dp[j])
    dp[i] += 1

print(dp)
print(T - max(dp))

