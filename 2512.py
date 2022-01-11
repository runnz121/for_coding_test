import sys
cnt = int(input())
arr = list(map(int, sys.stdin.readline().split()))
total = int(input())

low, high = 0, max(arr)

while low <= high:
    mid = (low + high)//2
    num = 0
    # 배열 원소가 mid값보다 크면 mid를 누적함
    for i in arr:
        if i >= mid:
            num += mid
    # 배열 원소가 mid값보다 작으면 원소값은 누적함
        else:
            num += i

    # 총 누적합이 주어진 total 값보다 작으면 low를 더함
    if num <= total:
        low = mid + 1
    # 아니면 high에서 1 빼줌
    else:
        high = mid -1
# 최대큰 값을 구해야 함으로 high를 출력
print(high)