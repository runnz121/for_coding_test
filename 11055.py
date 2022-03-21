
n = int(input())

arr = list(map(int, input().split()))

# dp 테이블을 그냥 리스트 그대로 설정
dp = [x for x in arr]


for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
