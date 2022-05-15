
def dfs(graph, v, visited):

# 1 2 7 6 8 3 4 5
    visited[v] = True #방문 처리
    print(v, end= ' ')

    for i in graph[v]: # v 는 1부터 graph[1] == [2,3,8] == i
        if not visited[i]: # 조건문이 해당하지 않는 경우에 실행 즉 true가 아니면 실행
            dfs(graph, i, visited) # 2가 전달됨


graph = [
    [], # 0번 노드
    [2,3,8], # 1번노드
    [1,7],   # 2번노드
    [1,4,5], # 3번노드
    [3,5], # 4번노드
    [3,4],# 5번노드
    [7],# 6번노드
    [2,6,8],# 7번노드
    [1,7]# 8번노드
]
visited = [False] * 9
dfs(graph, 1, visited)