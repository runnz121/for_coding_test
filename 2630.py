# line = int(input())
#
# board = [[] for _ in range(line)]
# for i in range(line):
#     board[i] = list(map(int, input().split()))
#
#
# # 좌표를 받아서 해당 좌표의 값이
# white, blue = 0, 0
#
# def divide(x, y, n):
#     global white, blue
#     color = board[x][y] # 현재 보드의 색깔(첫번째 위치의 색깔은 나중의 색깔과 같아야한다)
#     check = True # for문 탈출용
#
#     #row를 검색
#     for i in range(x, x+n):
#         if not check: # check가 false이면 탈출
#             break
#         #column 을 검색
#         #https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python
#         # 격자를 나누고 그 격자 안의 색깔이 모두 같은지를 검사
#         # 재귀시작시 처음 호출되는 부분의 위치값을 넣어주는게 중요
#         for j in range(y, y+n):
#             if color != board[i][j]:
#                 check = False
#                 #print(x, y, n//2,n)
#                 divide(x, y, n//2)# 1사분면
#                 divide(x, y+n//2, n//2)# 2사분면
#                 divide(x+n//2, y, n//2)# 3사분면
#                 divide(x+n//2, y+n//2, n//2)# 4사분면
#                 break
#     if check:
#         if color:
#             blue += 1
#         else:
#             white += 1
# divide(0,0,line)
# print(white)
# print(blue)
line = int(input())

board = [[] for _ in range(line)]
for i in range(line):
    board[i] = list(map(int, input().split()))


# 좌표를 받아서 해당 좌표의 값이
white, blue = 0, 0

def divide(x, y, n):
    global white, blue
    color = board[x][y] # 현재 보드의 색깔(첫번째 위치의 색깔은 나중의 색깔과 같아야한다)
    check = True # for문 탈출용

    #row를 검색
    for i in range(x, x+n):
        if not check: # check가 false이면 탈출
            break
        #column 을 검색
        #https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python
        # 격자를 나누고 그 격자 안의 색깔이 모두 같은지를 검사
        # 재귀시작시 처음 호출되는 부분의 위치값을 넣어주는게 중요
        for j in range(y, y+n):
            if color != board[i][j]:
                check = False
                #print(x, y, n//2,n)
                divide(x, y, n//2)# 1사분면
                divide(x, y+n//2, n//2)# 2사분면
                divide(x+n//2, y, n//2)# 3사분면
                divide(x+n//2, y+n//2, n//2)# 4사분면
                break
    if check:
        if color:
            blue += 1
        else:
            white += 1
divide(0,0,line)
print(white)
print(blue)