while True:
    arr = list(map(int, input().split()))
    if len(arr) == 0 or len(arr) == 1:
        break

    arr = arr[1:]

    stacks = []

    square = arr[0]
    mins = arr[0]
    max_stack = arr[0]
    stacks.append(arr[0])
    for i in range(1, len(arr)):
        # 다음게 큰거 -> 스택 인
        if stacks[-1] <= arr[i]:

            max_stacks = stacks[-1]

            comp_square = max(arr[i], max_cnt * max_stacks)

            square = max(square, comp_square)
            stacks.append(arr[i])


        # 다음게 작은거 -> 스택 아웃 -> 스택 인
        else:
            h = stacks.pop()
            h * (i - )


    print(square)