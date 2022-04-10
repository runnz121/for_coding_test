from collections import deque

# 노드, 간선 갯수 입력 받기
v, e = map(int, input().split())

indegree = [0] * (v + 1)

# 연결리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프 모든 간선 정보 입력 받기
for _ in range(e):
    a, b = map(int, input().split()) # 정점 a 에서 b로 이동 가능하다는걸 의미
    graph[a].append(b)
    #진입차수 증가시키기
    indegree[b] += 1

print(graph) # [[], [2, 5], [3, 6], [4], [7], [6], [4], []]
print(indegree) # [0, 0, 1, 1, 2, 1, 2, 1]

# 위상정렬함수
def topology_sort():
    result = [] #결과리스트 담기
    q = deque()

    # 처음 시작시 진입차수가 0 인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때가지
    while q:
        now = q.popleft()
        result.append(now)

        # 해당 원소에 연결된 노드의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 넣기
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()