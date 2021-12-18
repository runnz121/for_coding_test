T = int(input())

arr = list(map(int, input().split()))

dp1 = [0] * T
dp2 = [0] * T
dp1[0] = arr[0]
dp1[1] = arr[1]
dp2[1] = arr[1]
# arr[i] == 1 이거나, 감소하는 추세에서 이전값보다 큰게 나오면 해당 수에서 종료
cnt = 0
up = True


for i in range(T):
    max_val = arr[i]
    for j in range(i, T):
        if arr[j] > max_val:
            dp[]


print(dp1)