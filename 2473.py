import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

mins = sys.maxsize

# 용액 하나를 고정 시켜두고 포인터 두개를 움직임
for i in range(n - 2):
    # 시작 고정 용액은 arr[0]
    start = i + 1
    end = n - 1

    while start < end:
        sol = arr[i] + arr[start] + arr[end] # 용액의 합

        # 용액의 절대값이 현재 임의의 최대값보다 작은 경우
        if abs(sol) <= mins:
            mins = abs(sol)
            # 용액 상황 업데이트
            ans = [arr[i], arr[start], arr[end]]
        # 0보다 작으면 시작점을 증가
        if sol < 0:
            start += 1
        # 아니면 끝점을 줄임
        elif sol > 0:
            end -= 1
        # 0인 경우 종료
        else:
            break

print(ans[0], ans[1], ans[2])