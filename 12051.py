import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]

# 가장 큰 수랑 비교하기 위해 dp 배열에 마지막의 수와 비교
for i in arr:
    # 만약 dp 들어있던 값이 배열 값보다 작으면 dp에 추가
    if dp[-1] < i:
        dp.append(i)

    # 그게 아니라면 이분탐색 실행
    # 이분탐색 통해서 이 숫자가 어디 자리에 들어가야 할지 찾는다
    else:
        # dp 기준으로 인덱스로 구분
        left = 0
        right = len(dp)-1

        # 이분탐색 실행해서
        while left < right:
            mid = (left + right)//2

            # dp의 가운데 값 < 배열의 값 일 경우
            if dp[mid] < i:
                # 오른쪽에 다가 넣어야 함으로 왼쪽값 증가
                left = mid + 1
                # 그게 아니라면 오른쪽은 mid값이 된다
            else:
                right = mid
        # dp[mid == right] 는 배열의 해당 원소값이된다
        dp[right] = i

# dp에 0 이 들어있음으로 이값을 빼주고 길이를 계산
print(len(dp)-1)
print(dp)