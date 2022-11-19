import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

mins = sys.maxsize

# 용액 하나를 고정 시켜두고 포인터 두개를 움직여서 처리
for i in range(n - 2):
    start = i + 1
    end = n - 1

    while start < end:
        sol = arr[i] + arr[start] + arr[end]

        if abs(sol) <= mins:
            mins = abs(sol)
            ans = [arr[i], arr[start], arr[end]]
        if sol < 0:
            start += 1
        elif sol > 0:
            end -= 1
        else:
            break

print(ans[0], ans[1], ans[2])