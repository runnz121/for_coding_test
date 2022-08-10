import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

graph = []

time = int(1e9)
db = []

for i in range(N):
    x = list(map(int, input().split()))
    for k in x:
        if k not in db:
            db.append(k)
    graph.append(x)

db.sort()

dbs = [i for i in range(db[0],db[-1]+1)]

ans = []
# 블럭 기준
for std in list(dbs):
    tmp_time = 0
    inven = B
    for line in graph:
        for bricks in line:
            # 기준이 브릭보다 더 크면 -> 인벤에서 꺼냄
            if std > bricks:
                inven -= abs(std-bricks)
                tmp_time += 1 * abs(std-bricks)
            elif std < bricks:
                inven += abs(bricks-std)
                tmp_time += 2 * abs(bricks-std)

    if 0 <= std <= 256 and inven >= 0:
         ans.append([tmp_time, std])
    # else:
    #     continue
    # ans.append([tmp_time, std, inven])


ans.sort(key=lambda x : (x[0], -x[1]))
# if len(ans) >0:
#     print(*ans[0])
print(*ans[0])

#
# 3 4 11
# 29 51 54 44
# 22 44 32 62
# 25 38 16 2

# 7 7 6000
# 30 21 48 55 1 1 4
# 0 0 0 0 0 0 0
# 15 4 4 4 4 4 8
# 20 40 60 10 20 30 2
# 1 1 1 1 1 1 9
# 24 12 33 7 14 25 3
# 3 3 3 3 3 3 32