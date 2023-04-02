s, k = map(int, input().split())

maxx =  s//k + 1
ranges= [i for i in range(1, maxx + 1)]
check = [False] * (maxx + 1)


def back(depth):

    if depth == k:
        return

    for i in range(len(ranges)):
        