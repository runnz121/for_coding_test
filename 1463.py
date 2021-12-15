
N = int(input())

dp = [0] * 10000000
count = 0

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1 # 만약 2,3으로 안나뉘는 경우도 있을 수 있음으로 들어온 숫자에 1을 빼주고 횟수를 1더해줌 이걸 현재 값으로 지정
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i //3] + 1) # 최소값 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[N])