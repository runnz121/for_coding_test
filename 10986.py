
n, m = map(int, input().split())

arr = list(map(int, input().split()))
#
# dp = [[0] * n for _ in range(n)]

cnt = 0
for i in range(1, n):
    arr[i] += arr[i-1]
    if arr[i] % m == 0:
        cnt += 1

i = 0
while True:

    for k in range(i, n):
        if (arr[k] - arr[i]) % m == 0 and (arr[k] - arr[i]) != 0:
            cnt += 1

    i += 1

    if i == n-1:
        break

print(cnt)

# n, m = map(int, input().split())
#
# arr = list(map(int, input().split()))
#
# cnt = 0
# for i in range(1, n):
#     arr[i] += arr[i-1]
#
#
# for k in range(n):
#     arr[k] %= m
#
# print(arr)

# 누적합 배열을 m으로 나눔
# 1 0 0 1 0

# 주어진 배열
# 1 2 3 1 2


# 1 3 6 7 9
# 0 2 5 6 8
# 0 0 3 4 6
# 0 0 0 1 3
# 0 0 0 0 2


# https://zoosso.tistory.com/550
N, M = map(int, input().split())
a = list(map(int, input().split())) + [0]

# 나머지를 저장할 테이블
cnt = [0] * M

# 인덱스가 0인 것을 포함
cnt[0] = 1

for i in range(N):
    # 누적합을 처리
    a[i] += a[i - 1]

    # 각 나머지 종류의 갯수를 해당 테이블에 저장
    cnt[a[i] % M] += 1

#print(cnt)
ans = 0

# M 개 중에서 2개를 골라(누적합 특성상 i, j 차이를 말하는 것이기 때문) 더해주는거랑 같음 mC2
for k in cnt:
    ans += k * (k-1) // 2

print(ans)

# https://velog.io/@learningssik/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# import sys
# total, tar = map(int,sys.stdin.readline().split())
#
# tem = list(map(int,sys.stdin.readline().split()))
#
# prepix = [0 for i in range(tar)]
# presum = 0
#
# prepix[0] = 1
#
#
# for i in range(total):
#     presum+=tem[i]
#     # prepix.append(presum%tar)
#
#     prepix[presum%tar] += 1
#
# print(prepix)
# '''
# 나머지가 같은 두 부분합을 고르면 두 구간은 결국 tar의 배수가 된다.
# 나머지가 0인 경우는 부분합 자체가 tar의 배수인 경우이므로 두 구간이 아니라 본인 구간도 될 수 있기 때문에
# index가 0인 (부분합 0) 것을 포함
# '''
# ans=0
# for i in prepix:
#     ans += i*(i-1)//2
#
# print(ans)
