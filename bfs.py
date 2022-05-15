from collections import deque

#1 2 3 8 7 4 5 6
def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

bfs(graph, 1, visited)