import math

x, y = map(int, input().split())

# 확률 계산하기(실수연산을 틀릴 수 있기 때문에 애초에 100을 분자에 곱하고 시작)
z = math.floor(100*y / x)
low, high = 0, 1000000000

# 확률이 99보다 크면 -1 출력
if z >= 99:
    print(-1)
else:
    while low <= high:
        # mid = 추가로 게임을 진행해야하는 수
        mid = (low + high) // 2

        # mid 값을 바탕으로 새로운 확률을 계산하기
        tx, ty = x + mid, y + mid
        # 새로운 확률을 계산하였을 때 현재 승률 보다 높다면
        # 최대값 범위 감소 = mid값 감소
        if math.floor(100 *ty/tx) > z:
            high = mid - 1
        # 새로운 승률이 낮은 경우
        # 최대갑 범위 증가 = mid값 증가
        else:
            low = mid + 1
# 최소 게임 겟수에다가 +1을 해줌으로서 확률이 변화는 값을 출력
    print(high + 1)