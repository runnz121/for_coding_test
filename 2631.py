
# 최장 LIS 를 구해서 빼줌
n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(n)]


dp[0] = 1


for i in range(1, n):
    tmp_arr = []

    for j in range(i):

        if arr[i] > arr[j]:
            #다음 값이 더 크다면 그 값까지의 dp테이블의 값을 넣어줌
            tmp_arr.append(dp[j])
    if len(tmp_arr) == 0:
        dp[i] = 1
    else:
        # dp 테이블을 갱신
        dp[i] = max(dp[i], max(tmp_arr) + 1)

# 총 갯수에서 최장 길이의 갯수를 빼줌
print(n - max(dp))