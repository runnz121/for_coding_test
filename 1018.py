y, x = map(int, input().split())

arr = []
check = []
for _ in range(y):
    arr.append(input())

#8개씩 나누는 경우 -> 시작점을 잡는 반복문
for a in range(y - 7):
    for b in range(x - 7):
        idx1 = 0 #'W'로 시작할 경우 판의 갯수를 세기위함
        idx2 = 0 #'B'로 시작할 경우 판의 갯수를 세기위함
        for i in range(a, a+8): #위에서 적은 인덱스마다 1개씩 증가해서 슬라이딩으로 확인(8개씩)
            for j in range(b, b+8):
                #시작점과 색깔이 다르지 않은 경우에 체크
                if (i+j) % 2 == 0: #현재 행의 번호와 열의 번호합이 짝수이면 -> 시작점 색깔과 같아야 한다, 홀수면 다른색
                    if arr[i][j] != 'W':
                        idx1 += 1
                    if arr[i][j] != 'B':
                        idx2 += 1
                else:
                    if arr[i][j] != 'B':
                        idx1 += 1
                    if arr[i][j] != 'W':
                        idx2 += 1
        check.append(min(idx1,idx2))

print(min(check))

# N, M = map(int, input().split())
# original = []
# count = []
#
# for _ in range(N):
#     original.append(input())
#
# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))
#
# print(min(count))