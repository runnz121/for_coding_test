n, m = map(int, input().split())

graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

min_dis = int(1e9)

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])
        elif graph[i][j] == 1:
            house.append([i,j])

# 치킨 집 담을 배열
check = [False] * len(chicken)

tmp = []

def cal(chicks):

    tmp_dist = 0
    mins_dist = int(1e9)

    for k in house:
        for j in chicks:
            x, y = k[0], k[1]
            dx, dy = j[0], j[1]

            dist = abs(x-dx) + abs(y-dy)
        # 집 기준으로 최소 거리에 있는 치킨집
            mins_dist = min(dist, mins_dist)
        tmp_dist += mins_dist
    print("tmp_dist", tmp_dist)
    return tmp_dist



def back(depth, start):
    global tmp
    global min_dis

    # 치킨집을 골라서 반환
    if depth == m:
        min_dis = min(cal(tmp), min_dis)
        print("치킨집", tmp)
        return

    for i in range(start, len(chicken)):
        if check[i]:
            continue
        tmp.append(chicken[i])
        check[i] = True
        back(depth + 1, i)
        check[i] = False
        tmp.pop()

back(0, 0)

print(min_dis)
