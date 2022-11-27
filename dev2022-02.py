from collections import deque

def solution(low, high, img):
    answer = 0

    row = len(img[0]) # x
    col = len(img) # y

    dx = [-1,1,0,0,]
    dy = [0,0,-1,1]

    def bfs(x, y):
        check = [False for _ in range(row) for _ in range(col)]

        que = deque()
        que.append([x, y])

        while que:
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < row and 0 <= ny < col:
                    if not check[nx][ny]:
                        check[nx][ny] = True
                        que.append([nx, ny])

    for i in range(row):
        for j in range(col):
            if img[i][j] == '#':
                bfs(i, j)



    return answer



img = [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]
solution(25, 50 , img)