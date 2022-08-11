n = int(input())

arr = []

for i in range(n):
    x = list(map(int, input().split()))
    x.insert(0,0)
    arr.append(x)
arr.insert(0,[])

min_dist = int(1e9)

check = [False] * n
node = [i for i in range(1, n+1)]
graph = []
temp = []

def find_min(nodes):
    global min_dist
    global arr
    dist = 0
    flag = True
    for node in range(len(nodes)-1):
        if arr[nodes[node]][nodes[node+1]] == 0:
            flag = False
            break
        else:
            dist += arr[nodes[node]][nodes[node+1]]
    if flag:
        dist += arr[nodes[n-1]][nodes[0]]
        min_dist = min(dist, min_dist)
    else:
        return

def back(depth):

    global graph
    global temp

    if depth == n:
        #print(temp)
        find_min(temp)
        return

    for i in range(n):
        if check[i]:
            continue

        temp.append(node[i])
        check[i] = True
        back(depth + 1)
        temp.pop()
        check[i] = False

back(0)


print(min_dist)
