import sys

x = int(input())

arr = list(map(int, input().split()))
arr.sort()

left = 0
right = x-1

# 이거롤 안하면 에러남 (int(1e9)쓰지 말것
min_val = sys.maxsize

while left < right:
    res = arr[left] + arr[right]
    # 절대값 비교로 작으면 최소값 갱신, 답지에 넣어줌
    if abs(res) < min_val:
        min_val = abs(res)
        ans = [arr[left], arr[right]]

    # 절대값 씌우기 전의 값이 0보다 작다 -> 왼쪽 올려줌
    if res < 0:
        left += 1
    # 아니면 오른쪽 내려줌
    elif res > 0:
        right -= 1
    else:
        break

print(ans[0], ans[1])