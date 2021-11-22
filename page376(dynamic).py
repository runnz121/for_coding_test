n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

#2번째 리스트 부터 시작
for i in range(1, n):
    #해당 리스트 안의 원소를 탐색
    #range는 i+1 -1까지 돈다
    for j in range(i+1):
        #맨 왼쪽일 경우
        if j == 0:
            up_left = 0
        #맨왼쪽이나 오른족이 아니면 해당값을 저장
        else:
            up_left = dp[i-1][j-1]
        #맨 오른쪽일 경우
        if j == i:
            up = 0
        # 맨왼쪽이나 오른족이 아니면 해당값을 저장
        else:
            up = dp[i-1][j]
        #둘중에서 큰 값을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)
        print("i=",i, "j=",j,"up_left=", up_left,"up=",up, "dp[i][j] = " ,dp[i][j])
print(max(dp[n-1]))