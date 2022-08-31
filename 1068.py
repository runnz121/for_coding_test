# n = int(input())
#
# graph = list(map(int, input().split()))
#
# m = int(input())
#
# tree = [[] for _ in range(n)]
#
# check = [False] * n
# check[0] = True
#
# for i in range(len(graph)):
#     if graph[i] > -1:
#         tree[graph[i]].append(i)
#
#
# def dfs(start):
#     check[start] = True
#
#     for k in tree[start]:
#         if not check[k]:
#             dfs(k)
#
# dfs(m)
#
# for idx in tree:
#     for j in idx:
#         if tree[j]:
#             check[j] = True
#
# print(tree)
# print(check)
#
#
# cnt = 1
# for idx in check:
#     if idx == False:
#         cnt += 1
#
# print(cnt)


import sys

input = sys.stdin.readline


def dfs(v):
    tree[v] = -2
    for i in range(n):  # 전체 트리 반복
        if v == tree[i]:  # 지우고자 하는 노드 v가  tree[i]에 들어있으면 tree[i]는 v의 자식
            dfs(i)  # i의 자식도 지움


n = int(input())
tree = list(map(int, input().split()))  # [-1, 0, 0, 1, 1]
erase = int(input())

dfs(erase)
cnt = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:  # -2는 지우는 노드들 // i노드의 자식이 트리 안에 없으면 == 리프노드임
        cnt += 1

print(cnt)