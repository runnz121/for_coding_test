import sys

input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)] # 입력받은 알파벳을 숫자로 바꿈
alpha = [0] * 26 # 이게 체크배열 역할


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, count):
    global ans
    ans = max(ans, count) # 최대값 확인은 여기서 한번만
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alpha[arr[nx][ny]] == 0: # 범위를 벗어나지 않고, 체크배열에 중복되지 않음
            alpha[arr[nx][ny]] = 1 # 체크배열을 체크하고 재귀
            dfs(nx, ny, count + 1)
            alpha[arr[nx][ny]] = 0


ans = 1
alpha[arr[0][0]] = 1
dfs(0, 0, 1)

print(ans)


# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# arr = []
# for i in range(a):
#     res = list(map(str, input()))
#     arr.append(res)
# check = [[False] * b for _ in range(a)]
# check[0][0] = True
# ans = [arr[0][0]]
# cnt = 1
# anss = 1

# def dfs(x, y):
#     global cnt
#     global ans
#     global anss
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx < 0 or ny < 0 or nx >= a or ny >= b:
#             continue
#         if check[nx][ny]:
#             continue
#         check[nx][ny] = True
#         if arr[nx][ny] in ans:
#             check[nx][ny] = False
#             anss = max(cnt, anss)
#             continue
#         else:
#             ans.append(arr[nx][ny])
#             cnt += 1
#             dfs(nx, ny)
#             check[nx][ny] = False
#             ans.pop()
#             cnt -= 1
# dfs(0, 0)
#
# print(anss)