T = int(input())

arr = list(map(int, input().split()))

max_val = max(arr)
dp = [arr[0]]

#dp값과, arr의 다음 인덱스 값과 비교해서 더 큰 값을 넣어줌
for i in range(T-1):
    dp.append(max(dp[i] + arr[i+1], arr[i+1]))
print(max(dp))