import sys

n = int(input())

# 메모리 제한으로 전 시점과 현 시점의 최적해만 가지고 다닐 DP 선언
a, b, c = map(int, sys.stdin.readline().split())
max_dp = [a, b, c]
min_dp = [a, b, c]

# 현재 계단 이전에 선택할 수 있는 최적해 + 현재 계단의 값
for i in range(1, n):
    a, b, c = map(int, sys.stdin.readline().split())
    # 갈수 있는 방향은 총 3 군데임으로 케이스를 분리
    for j in range(3):
        if j == 0:
            max_first = max(max_dp[j], max_dp[j + 1]) + a
            min_first = min(min_dp[j], min_dp[j + 1]) + a
        if j == 1:
            max_second = max(max_dp[j - 1], max_dp[j], max_dp[j + 1]) + b
            min_second = min(min_dp[j - 1], min_dp[j], min_dp[j + 1]) + b
        if j == 2:
            max_third = max(max_dp[j - 1], max_dp[j]) + c
            min_third = min(min_dp[j - 1], min_dp[j]) + c
    max_dp = [max_first, max_second, max_third]
    min_dp = [min_first, min_second, min_third]

print(max(max_dp), min(min_dp))