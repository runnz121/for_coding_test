from collections import deque

n, m = map(int, input().split())

arr = []

check = [False] * 101

while True:
    try:
        x, y = map(int, input().split())
        arr.append([x, y])
    except:
        break

arr_1 = []
arr_2 = []

# 출발, 도착지 분리
for idx in arr:
    arr_1.append(idx[0])
    arr_2.append(idx[1])

check[0] = True

# 100에 도달하는 방법 저장
ans = []

# dp
dp = [0 for i in range(101)]

def bfs(start):
    q = deque()
    q.append(start)

    cnt_mid = -1

    while q:
        current = q.popleft()

        # 100 이면 횟수 저장
        if current == 100:
            ans.append(cnt_mid)

        # check이고, 100 이하일 경우
        if not check[current] and current <= 100:
            check[current] = True

            # 칸에 값이 존재할 경우
            if current in arr_1:
                idx = arr_1.index(current)
                q.append(arr_2[idx])
                # 주사위 횟수 증가
                dp[arr_2[idx]] = min(dp[arr_2[idx]]+1, dp)

            # 주사위로 이동(모든 가짓수를 다 넣어줌)
            else:
                # 주사위 횟수 증가
                cnt_mid += 1
                for i in range(1, 7):
                    next = current + i
                    if next <= 100 and check[next] == False:
                        q.append(next)

bfs(1)

print(ans)