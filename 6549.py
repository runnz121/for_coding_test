while True:
    arr = list(map(int, input().split()))
    if len(arr) == 0 or len(arr) == 1:
        break

    arr = arr[1:]

    stacks = []

    square = arr[0]

    stacks.append(arr[0])
    for i in range(1, len(arr)):
        # 다음게 큰거
        if stacks[-1] <= arr[i] and len(stacks) > 0:
            comp_square = max(stacks[-1], square, arr[i])
            if comp_square > square:
                square = comp_square
                if stacks[-1] != arr[i]:
                    stacks.pop()
                stacks.append(arr[i])
                mins = arr[i]

        # 다음게 작은거
        else:
            if len(stacks) == 0:
                continue
            while True:
                idx = len(stacks)-1
                if stacks[idx] < arr[i]:
                    comp_square = (len(stacks) - idx + 1) * arr[i]
                    square = max(comp_square, square)
                    break
                idx -= 1
                if idx < 0:
                    break


    print(square)