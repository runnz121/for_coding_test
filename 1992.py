line = int(input())

board = [[] for _ in range(line)]
for i in range(line):
    board[i] = list(map(int, input()))

ans =''
def div(x, y, n):
    global ans
    white = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if white != board[i][j]:
                ans += '('
                div(x, y, n//2)
                div(x, y+n//2, n//2)
                div(x+n//2, y, n//2)
                div(x+n//2, y+n//2, n//2)
                ans +=')'
                return
    #재귀함수로 안들어가고 for문이 끝난다면 서로 다른 값임으로 그냥 해당 값을 더해줌
    ans += str(white)

div(0,0, line)
print(ans)
