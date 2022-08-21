import copy

graph = []

for i in range(9):
    arr = list(map(str, input().split()))
    graph.append(arr)

arr = [i for i in range(1, 10)]

check = [False] * 9

tot = [[] for _ in range(9)]
tmp = []

def back(depth, line, idx):

    global tmp
    global tot

    tmp1 = copy.deepcopy(tmp)

    if depth == 9:
        flag = True
        line = list(line)
        for i in range(9):
            if line[i] != '0':
                if line[i] != str(tmp1[i]):
                    flag = False
                    break
        if flag:
            tot[idx].append(tmp1)
        return

    for i in range(9):
        if check[i]:
            continue

        tmp.append(arr[i])
        check[i] = True
        back(depth + 1, line, idx)
        tmp.pop()
        check[i] = False

for i in range(9):
    back(0, graph[i][0], i)

ans = []
for x in range(9):

print(tot)