n, k = map(int, input().split())

arr = []
dp = [0 for i in range(k+1)]

for i in range(n):
    arr.append(int(input()))

dp[0] = 1

# 어떤 임의의 coin으로 i원 만들기 ->  i원 - coin 원을 만든 후 coin원을 추가하는것과 같다
# 예를 들면 4원을 만들고 싶을때, 1원으로 4원을 만드는 수는 이미 1가지가 있다.
# 2원으로 4원을 만드는 수는 2 가지가 있는데, 이는 2원을 만드는 갯수와 같다
# 따라서 이러한 규칙을 보게되면  dp[4] = 4 - 2(i원 - 주어진coin) 이 됨을 알 수 있다.

for i in arr:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i] # dp[6] 일때 dp[5] + dp[4] + dp[1]

print(dp[k])