n = int(input())

# 각 수마다 각 자리수 앞에올 수 있는 갯수를 담는 테이블
dp = [[0] * 10 for i in range(n)]

# dp 테이블 초기화
dp[0] = [1 for i in range(10)]

for i in range(1, n):
    sum = 0
    for j in range(10): # 1
        for k in range(j + 1): # 0, 1
            dp[i][j] += dp[i-1][k] # 해당 테이블의 갯수는 이전 자릿수의 해당 끝자리수까지의 누적합이랑 같다
            sum += dp[i - 1][k]

if n==1:
    print(10)
else:
    print(sum%10007)



# 9 - 0  = 10 10
# 99 - 10 = 90 45
# 999 - 100 = 900 165
# 9999 - 1000 = 9000



# 9 - 0 = 10 10 1/1
#
# 99 - 10 = 90 45 1/2
#
# 999 - 100 = 990 165 1/6
#
#                       1/24