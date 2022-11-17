from collections import deque

# 테케
test = int(input())

for _ in range(test):

    # 노드, 간선 갯수
    n, k = map(int, input().split())

    # 각 건물 완성되는데 걸리는 시간
    build_time = [0] + list(map(int, input().split()))

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

    # dp 세팅
    dp = [0 for _ in range(n + 1)] # 해당 건물까지 걸리는 시간

    # 위상 정렬 함수
    def topology():
        global result
        q = deque()

        # 0 번 인덱스 제외 -> 0인 진입차수 넣기
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                # dp 테이블에 현재 인덱스의 건물이 지어지는 시간을 저장
                dp[i] = build_time[i]

        while q:
            now = q.popleft()
            result.append(now) # 결과에 deque 한것을 추가

            # 진입 차수를 -1
            for i in graph[now]:
                indegree[i] -= 1
                # dp 테이블 갱신을 하는데, 진입차수가 감소되는 인덱스기준으로 건물짓는데 더 오래 걸리는 것으로 설정
                dp[i] = max(dp[now] + build_time[i], dp[i])

                # 진입차수가 0이면 다시 ㅓㅎ음
                if indegree[i] == 0:
                    q.append(i)
    topology()

    print(dp[buildtowin])