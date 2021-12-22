n = int(input())

#dp[ N의 수 ][ N 자리 숫자일 때 해당 숫자 앞에 올 수 있는 일의 자리 수 ]

# 0 앞에 올 수 있는 숫자는 1 밖에 없고,
# 9 앞에 올 수 있는 숫자는 8 밖에 없지만
# 그 외에 2~8까지는 ±1한 숫자 2개가 올 수 있다.

# j가 0 일 때, dp[i][j] = dp[i-1][j+1]
# j가 9 일 때, dp[i][j] = dp[i-1][j-1]
# j가 2~8 일 때, dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

dp = [[0] * 10 for _ in range(n + 1)]

# 1 자리수는 0을 제외하고(조거 : 0은 앞에 올 수 없음) 1로 초기화
for i in range(1,10):
    dp[1][i] = 1

# dp[N 자리 수][N자리 숫자일 때 해당 Index 앞에 올 수 있는 일의 자리 수]
# 2 자리수부터 시작
for i in range(2, n+1): # n 자리 수
    for j in range(10): # Index
        # 뒷자리가 0일 때는 앞에 1밖에 오지 못함
        if j == 0 : dp[i][j] = dp[i-1][j+1]
        # 뒷자리가 9일 때는 앞에 8밖에 오지 못함
        elif j == 9 : dp[i][j] = dp[i-1][j-1]
        # 뒷자리가 2~8일 때는 앞에 숫자가 2개씩 올 수 있음
        else : dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n]) % 1000000000)