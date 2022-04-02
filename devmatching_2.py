import copy
from collections import deque


def solution(grid):
    q = deque()
    arr = []

    for i in grid:
        arr.append(list(i))


    globalcheck = [[False] * len(arr[0]) for _ in range(len(arr))]
    abc = ['a', 'b', 'c']

    answer = 0

    def bfs(a, b, k):

        count = 0

        q.append([a, b])
        check = [[False] * len(arr[0]) for _ in range(len(arr))]
        arr_cp = copy.deepcopy(arr)
        check[a][b] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):

                    if arr_cp[nx][ny] == k and check[nx][ny] == False:
                        count += 1
                        check[nx][ny] = True
                        q.append([nx, ny])
                    elif arr_cp[nx][ny] == '?' and check[nx][ny] == False:
                        arr_cp[nx][ny] = k
                        check[nx][ny] = True
                        q.append([nx, ny])
        return count

    for i in range(len(grid)):
        for j in range(len(grid)):
            if arr[i][j] == '?':
                for k in abc:
                    res = bfs(i, j, k)
                    print(res, i, j, k)
                    if res >= 1:
                        answer += 1
    print(arr)
    print(answer)
    return answer


grid = ["??b", "abc", "cc?"]
solution(grid)
