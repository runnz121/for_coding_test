n, m = map(int, input().split())

arr1 = [[] * m for _ in range(n)]

for i in range(n):
    arr1[i] = list(map(int, input().split()))

x, y = map(int, input().split())

arr2 = [[] * y for _ in range(x)]

for i in range(x):
    arr2[i] = list(map(int, input().split()))

#print(arr1, arr2)

ans = [[0] * y for _ in range(n)]
# 행열의 곱셈 N * M 행렬과 M * K 행렬 곱하면 N * K 행렬이 만들어진다
#
for i in range(n):
    for j in range(y):
        for k in range(m):
            ans[i][j] += arr1[i][k] * arr2[k][j]


for k in ans:
    print(*k)

# N, M = map(int, input().split())
# A = []
# for _ in range(N):
#     A.append(list(map(int, input().split())))
#
# M, K = map(int, input().split())
# B = []
# for _ in range(M):
#     B.append(list(map(int, input().split())))
#
# print(A, B)
#
# #행렬 곱셈
# C = [[0 for _ in range(K)] for _ in range(N)]
#
# for n in range(N):
#     for k in range(K):
#         for m in range(M):
#             C[n][k] += A[n][m] * B[m][k]
#
# #출력문
# for i in C:
#     for j in i:
#         print(j, end = ' ')
#     print()