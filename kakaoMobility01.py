def solution(flowers):
    answer = 0

    lens = len(flowers)

    sorts = sorted(flowers, key=lambda x: x[1])

    days = [False for _ in range(0, sorts[lens - 1][1])]

    for flower in flowers:
        for k in range(flower[0], flower[1]):
            days[k] = True

    for x in days:
        if x == True:
            answer += 1
    return answer


flowers = [[2, 5], [3, 7], [10, 11]]
solution(flowers)
