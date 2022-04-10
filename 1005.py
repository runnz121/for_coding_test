from collections import deque

# 테케
test = int(input())

# 노드, 간선 갯수
n, k = map(int, input().split())

# 각 건물 완성되는데 걸리는 시간
build_time = list(map(int, input().split()))

# 진입차수 0 초기화
indegree = [0] * (n + 1)
# 각 빌딩정보 담기
graph = [[] for i in range(n + 1)]

# 정보 받기
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 이기기 위해 지어야 할 건물
buildtowin = int(input())

result = []

def topology():
    global result
    q = deque()

    # 0 번 인덱스 제외 -> 0인 진입차수 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        if now == buildtowin:
            break

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
topology()

sums = 0

print(build_time)
print(sums)
