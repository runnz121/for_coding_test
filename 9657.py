n = int(input())
dp = [0]*1001
dp[1],dp[2],dp[3],dp[4] = "SK","CY","SK","SK"
stones = [1,3,4]


for i in range(5,n+1):
    for s in stones:
        if dp[i-s] == "CY":
            dp[i] = "SK"
            break
        dp[i] = "CY"

print(dp[n])