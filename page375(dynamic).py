#테스트 케이스 입력
for tc in range(int(input())):

    #금광정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    #dp테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    print(dp)

    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            #왼쪽 아래서 오는경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            #왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            print('i = ', i, 'left_up =', left_up, 'left_down =', left_down, 'left =',left, 'i,j =', i,j)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)


# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2