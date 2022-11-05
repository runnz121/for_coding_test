n = int(input())
building = list(map(int, input().split()))

row = [[0] * n for i in range(n)]

# i건물과 j 건물 사이 기울기
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        row[i][j] = (building[i] - building[j]) / (i - j)

max_val = 0
for i in range(n): # i = 4 -> 모든 건물 탐색을 위함
    cnt = 0
    # 왼쪽에서 볼 수 있는 것 -> 기준건물까지
    for j in range(i): # j = 0 ~ 4
        possi = True
        # 기준 건물과 상대 건물 사이 중간에 있는 건물을 말함
        for k in range(j + 1, i): # k = 1 ~ 4, k = 2 ~ 4....
            if row[k][i] <= row[j][i]: # 기준 건물과 상대 건물 사이에 있는 건물의 기울기가 작다면 볼 수 없다!
                possi = False
        if possi:
            cnt += 1
    # 오른쪽에서 볼 수 있는 것 -> 기준 건물부터 시작
    for r in range(i + 1, n): # 5 ~ 14
        possi = True
        for x in range(i + 1, r): # 4 ~ 5, 4 ~ 6 ...
            if row[i][x] >= row[i][r]:
                possi = False
        if possi:
            cnt += 1
    max_val = max(max_val,cnt)

print(max_val)