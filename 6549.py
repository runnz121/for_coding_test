while True:
    N, *rect = map(int, input().split())

    if N == 0:
        break

    square = 0
    stacks = []


    for i in range(N):
        mins = i
        while stacks and stacks[-1][0] >= rect[i]:
            h, mins = stacks.pop()
            tmp_size = h * (i - mins)
            square = max(square, tmp_size)
        stacks.append([rect[i], mins])

    for h, point in stacks:
        square = max(square, (N- point)*h)


    print(square)
