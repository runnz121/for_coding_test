
n = int(input())
m = int(input())

# m 보다 작은 숫자의 갯수를 찾는것이 목적
# 이미 특정 숫자를 지정하고 이 숫자가 k 번째 숫자인지
# 확인하는 것

start, end = 1, m

while start <= end:
    mid = (start + end) //2


# i * j에서 i 행에 속해 있는 숫자는 모두 i의 배수이다
# 따라서 min(mid/i, n)이 i 번째 행에서 mid보다 작은 숫자들의 갯수가됨(임의의 m 보다 작은)
    tmp = 0
    # 인덱스 1부터 시작하고, N * N 배열임으로 N개까지 범위
    # mid가 N*N에서 몇번째로 큰 숫자인지 알 수 있다
    for i in range(1, n+1):
        tmp += min(mid//i, n) # mid 이하의 i의 배수 or 최대 n

    # tmp가 m보다 크다면(우리가 구할려는 수보다)
    # 앞부분을 검새한다
    if tmp >= m: # 이분탐색 실행
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)