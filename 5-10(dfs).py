n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):

    if x <= -1 or x >= n or y <= -1 or y > m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리
        #상하좌우로 탐색함
        dfs(x-1, y)#상
        dfs(x, y-1)#좌
        dfs(x+1, y)#하
        dfs(x, y+1)#우
        return True #0임으로 True로 반환
    return False #1이라는거니깐 false로 반환

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)

