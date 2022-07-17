n, m = map(int, input().split())


graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

min_dis = int(1e9)

chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])

# 치킨 집 담을 배열
check = [False] * len(chicken)

tmp = []

def cal(arr):

    temp_ans = int(1e9)
    temp_ans1 = 0
    # 치킨집 백트랙킹으로 모음
    for k in arr:
        x = k[0]
        y = k[1]

        # 최소값 더할 변수
        tmp_sum = int(1e9)
        # 전체 그래프 돌면서 해당 치킨집 기준 최소 치킨 거리 계싼
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    tmp_sum = abs(x-i) + abs(y-j)
                    temp_ans1 += tmp_sum
                    #tmp_sum = min(abs(x-i) + abs(y - j), tmp_sum)
        temp_ans = min(temp_ans1, temp_ans)
    # 전체 최소값 반환
    return temp_ans


def back(depth, start):
    global tmp
    global min_dis

    if depth == m:
        #min_dis += min(cal(tmp), min_dis)
        min_dis = min(cal(tmp), min_dis)
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