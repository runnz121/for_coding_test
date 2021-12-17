T = int(input())

arr = list(map(int, input().split()))
arr.insert(0,0)

dp1 = [0] * T
dp2 = [0] * T
dp1[1] = arr[1]
dp2[1] = arr[1]
# arr[i] == 1 이거나, 감소하는 추세에서 이전값보다 큰게 나오면 해당 수에서 종료
cnt = 0
up = True

for p1, p2 in zip(arr, arr[1:]):
    if p1 < p2:
        cnt += 1
    elif p1 > p2:
        dp[p1]