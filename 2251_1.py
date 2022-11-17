from collections import deque

q = deque()
q.append([0, 0])

check = [[False] * 201 for _ in range(201)]
check[0][0] = True

answer = []

a, b, c = map(int, input().split())


def pour(x, y):
    if not check[x][y]:
        check[x][y] = True
        q.append([x,y])

def bfs():

    while q:
        # a, b로만 놓고 봄
        a1, b1 = q.popleft()
        c1 = c - a1 -b1

        # a가 없는 경우 답 저장
        if a1 == 0:
            answer.append(c1)

        # a -> b 로 물 이동
        res = min(a1, b - b1)
        pour(a1 - res, b1 + res)

        # a -> c 로 물 이동
        res = min(a1, c - c1)
        pour(a1 - res, b1)

        # b -> a 로 물 이동
        res = min(b1, a - a1)
        pour(a1 + res, b1 - res)

        # b -> c 로 물 이동
        res = min(b1, c - c1)
        pour(a1, b1 - res)

        # c -> a 로 물 이동
        res = min(c1, a - a1)
        pour(a1 + res, b1)

        # c -> b 로 물 이동
        res = min(c1, b - b1)
        pour(a1, b1 + res)

bfs()

answer.sort()
print(*answer)