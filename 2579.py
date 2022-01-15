N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:# dp 초기화
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    #현재 기준 3칸 밑에서 올라오는 것과, 2칸 밑에서 올라오는것 기준으로 큰값이 현재 값
    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[N])
    print(dp[0])