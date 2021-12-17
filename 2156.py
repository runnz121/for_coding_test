T = int(input())
#인덱스 보정을 위해 0부터 추가
arr = [0]
for i in range(T):
    arr.append(int(input()))

if T == 1:
    print(arr[1])
else:
    dp = [0] * (T+1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    # 이전  dp값이랑 비교해서 도 max인지를 확인
    # 현재 기준 3칸 밑에서 올라오는 것과, 2칸 밑에서 올라오는것 기준으로 큰값이 현재 값
    for i in range(3, T+1):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

    print(max(dp))
# print('arr', arr)
# print('dp', dp)