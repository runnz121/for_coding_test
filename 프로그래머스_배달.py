def solution(N, road, K):
    answer = 0

    graph = [[0] * (N+1) for _ in range(N+1)]

    for i in road:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]

    def dfs(idx, num, check):
        nonlocal answer
        if num <= K:
            check[idx] = True
            answer += 1
        else:
            return
#graph[idx]
        for x in range(1, N+1):
            if graph[idx][x] != 0 and check[x] == False:
                return dfs(x, graph[idx][x] + num, check)

    for k in range(1, N+1):
        check = [False] * (N + 1)
        if graph[1][k] != 0:
            dfs(k, graph[1][k], check)

    print(answer)
    return answer


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N, road, K)