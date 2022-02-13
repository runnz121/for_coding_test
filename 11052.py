n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        # 자기 자신의 경우, 카드 팩 갯수일때읭 인덱스 + dp[인덱스 - 카드팩갯수]
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])