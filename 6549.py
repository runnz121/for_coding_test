while True:
    N, *rect = map(int, input().split())

    if N == 0:
        break

    square = 0
    stacks = []


    for i in range(N):
        mins = i

        # 현재 스택에 있는 것보다 다음에 들어올 직사각형 높이가 더 작을 경우 -> pop
        while stacks and stacks[-1][0] >= rect[i]:

            h, mins = stacks.pop()

            # 스택에 빠져 나온 직사각형의 높이와 갯수만큼 넓이를 갱신 시켜준다
            tmp_size = h * (i - mins)
            square = max(square, tmp_size)

        # 현재 스택에 있는 것보다 다음에 들어오는 것보다 클 경우 -> append
        stacks.append([rect[i], mins])

    # 스택에 남아 있는 경우 -> 해당 갯수만큼 높이를 갱신
    for h, point in stacks:
        square = max(square, (N - point)*h)


    print(square)
