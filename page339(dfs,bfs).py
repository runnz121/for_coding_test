from collections import deque

n,m,k,x = map(int, input().split())

#도시 갯수만큼 빈배열 생성하고
graph = [[] for _ in range(n+1)]

#도시에 연결된 노드를 리스트로 받는다
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

#거리 초기화(거리 이동시 +1 해줄거임)
distance = [-1] * (n + 1)
distance[x] = 0


#시작 노드값을 넣어준다
q = deque([x])
while q:
    now = q.popleft()

    for next_node in graph[now]:
        print("next_node", next_node)
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            print("distance", distance)
            q.append(next_node)


check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)