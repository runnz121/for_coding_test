x = int(input())

arr = list(map(int, input().split()))

arr = arr[::-1]

print(arr)

dp = [1] * x

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            print(f'i: {i},j: {j}, DP: {dp}')

print(max(dp))