from collections import deque

N, M, B = map(int, input().split())

graph = []

time = 0
height = 0

db ={}

for i in range(N):
    x = list(map(int, input().split()))
    graph.append(x)

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] in db:
            db[graph[i][j]] += 1
        else:
            db[graph[i][j]] = 1
# 그래프 순회하고 그래프에 들어있는 값들을 지정
# 해당 블럭의 갯수가 적고, 블럭 높이 오름차순 정렬
sorted_db = sorted(db.items(), key = lambda x : (x[1], -x[0]))

print(sorted_db)

# 전체 범위
total = N * M

answer = [0,0]

max_height = sorted_db[len(sorted_db)-1][0]

flag = False

for key, value in sorted_db:
    if B >= value:
        if key > max_height:
            answer[0] = value * 2
        else:
            answer[0] = value * 1
        flag = True
        answer[1] = max_height
        break


sorted_db = sorted(db.items(), key = lambda x : (-x[1], x[0]))

print("second", sorted_db)

if not flag:
    answer[0] = sorted_db[0] * 2
    answer[1] = sorted_db[len(sorted_db)-1]


print(*answer)
