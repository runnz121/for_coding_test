n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(input())

a, b = 0, 0

# 행
for i in range(n):
    if "X" not in board[i]:
        a += 1

# 열
for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:
        b += 1

# x 가 안들어있는 것중 최대값 출력
print(max(a ,b))