n = int(input()) # 전체상담갯수
t = [] # 상담 완료하는데 거리는 기간
p = [] # 각 상담 완료시 받을 수 있는 금액
dp = [0] * (n+1) # dp 테이블 초기화
max_value = 0 #뒤에서 부터 날짜를 따질때 현재까지의 최대 상담 금액에 해당하는 변수

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
print(t,p)

# 리스트를 뒤에서부터 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
        print(dp[i], max_value)
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)