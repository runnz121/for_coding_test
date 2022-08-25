from collections import deque

n, m = map(int, input().split())

arr = []

check = [False] * 101
board = [0] * 101

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
check[1] = True

# 100에 도달하는 방법 저장
ans = []

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        current = q.popleft()

        # 100 이면 횟수 저장
        if current == 100:
            print(board[current])
            break

        for i in range(1, 7):
            next = i + current

            if next in arr_1:
                idx = arr_1.index(next)
                next = arr_2[idx]

            if next <= 100 and not check[next]:
                board[next] = board[current] + 1
                q.append(next)
                check[next] = True
bfs(1)
