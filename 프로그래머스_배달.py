def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    graph1 = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in road:
        graph1[i[0]][i[1]] = min(i[2], graph1[i[0]][i[1]])
        graph1[i[1]][i[0]] = min(i[2], graph1[i[1]][i[0]])

    selfs = []
    print(graph1)

    def dfs(idx, num, check):
        nonlocal answer
        nonlocal selfs

        if num <= K:
            check[idx] = True
            selfs.append(idx)
            answer += 1
        else:
            return

        for x in range(1, N + 1):
            if graph1[idx][x] != INF and check[x] == False:
                dfs(x, graph1[idx][x] + num, check)

    for k in range(1, N + 1):
        check = [False] * (N + 1)
        check[0] = True
        check[1] = True
        if graph1[1][k] != INF:
            dfs(k, graph1[1][k], check)


    s = set(selfs)
    answer = len(s) + 1
    return answer


N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
solution(N, road, K)
