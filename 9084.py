case = int(input())

for i in range(case):

    x = int(input())
    list_case = list(map(int, input().split()))
    make = int(input())

    dp = [0] * (make + 1)
    dp[0] = 1

    for case in list_case:
        for i in range(1, make + 1):
            if i >= case:
                dp[i] += dp[i - case]
    print(dp[make])

