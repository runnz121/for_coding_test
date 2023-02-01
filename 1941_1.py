from sys import stdin

def permutation(idx, ans, position):
    global cnt, check

    if ans.count('Y') > 3:
        return

    if idx == 7:
        if ans.count('S') >= 4:
            check_p(position[0], position)
            # 이중 리스트 요소의 합 구하기 (
            if sum(sum(check, [])) == 7:
                cnt += 1
            check = [[0] * 5 for _ in range(5)]
        return
    # 조합을 만듬
    for i in range(25):
        if visit[i] == 0:
            visit[i] = 1
            permutation(idx + 1, ans + arr[i], position + [i])
            for j in range(i + 1, 25):
                visit[j] = 0


def check_p(s, position):
    x = s//5
    y = s%5

    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            next = nx * 5 + ny
            if check[nx][ny] == 0 and next in position:
                check[nx][ny] = 1
                check_p(next, position)


arr = []
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(5):
    arr += list(map(str, stdin.readline().strip()))
print(arr)
visit = [0 for _ in range(25)]
check = [[0] * 5 for _ in range(5)]
permutation(0, '', [])
print(cnt)