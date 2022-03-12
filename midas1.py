def solution(H):
    answer = []

    maxh = max(H)
    minh = min(H)
    lens = len(H)



    for i in range(minh, maxh + 1):
        stack = []
        sums = 0
        duple = 0
        for j in range(len(H)):
            if H[j] >= i:
                stack.append(H[j])
            if H[j] < i or j == lens-1:
                if i in stack:
                    while stack:
                        #print(i, stack.count(i))
                        sums += len(stack)
                        res = stack.pop()
                        if res > i:
                            duple += 1
                        du = stack.count(i)
                        if du >= 2:
                            duple += du -1
                else:
                    continue

        answer.append([i, sums - duple])
    print(answer)
    return answer


H = [3,2,1,1,3]
solution(H)