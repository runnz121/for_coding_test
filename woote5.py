def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)]
    flag = 0

    # 행/열
    # rows/columns
    ans = write(graph, 0, 0, 1)
    flag = check(graph, rows, columns)
    print(ans)
    return ans


def write(graph, x, y, current):
    flag = check(graph, rows, columns)
    if flag == 0:
        ans = graph
        return ans
    else:
        if current % 2 == 0:
            current += 1
            if x + 1 == rows:
                x = -1
            graph[x + 1][y] = current
            x = x + 1
        else:
            current += 1
            if y + 1 == columns:
                y = -1
            graph[x][y + 1] = current
            y = y + 1
        return write(graph, x, y, current)


def check(graph, rows, columns):
    zero_cnt = 0
    for i in range(rows):
        for j in range(columns):
            if graph[i][j] == 0:  # 0이 있으면 1이상 0이 없으면 0반환
                zero_cnt += 1
    return zero_cnt


rows = 3
columns = 4

rows1 = 3
columns1 = 3

print(solution(rows, columns))
