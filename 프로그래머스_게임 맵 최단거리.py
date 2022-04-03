from collections import deque


def solution(maps):
    arr = [[0] * len(maps[0]) for _ in range(len(maps))]

    q = deque()

    def bfs(a, b):
        q.append([a, b])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):  # maps 인덱스 탐색 조건
                    if maps[nx][ny] == 1:  # 길인 경우에만 탐색
                        arr[nx][ny] = arr[x][y] + 1
                        arr[nx][ny] = min(arr[nx][ny], arr[x][y] + 1)
                        q.append([nx, ny])
                        maps[nx][ny] = -1

    bfs(0, 0)

    answer = arr[len(maps) - 1][len(maps[0]) - 1]

    if answer == 0:
        answer = -1
    else:
        answer += 1

    return answer


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
solution(maps)
