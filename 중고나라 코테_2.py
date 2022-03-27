from collections import deque

def solution(board):
    answer = 0
    cp = [[0] * 4 for _ in range(4)]


    def bfs(x, y):
        q = deque()
        q.append([x, y])
        check = [[False] * 4 for _ in range(4)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        while q:
            x, y = q.popleft()
            check[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    if board[nx][ny] == board[x][y] and check[nx][ny] == False:
                        cp[x][y] = max(cp[x][y], cp[nx][ny] + 1)
                        q.append([nx, ny])


    for i in range(4):
        for j in range(4):
            bfs(i, j)


    for i in cp:
        if max(i) == 0:
            return -1
        else:
            answer = max(i)

    return answer


board =[[4,2,3,2], [2,1,2,4], [1,2,3,1], [4,1,4,3]]
solution(board)