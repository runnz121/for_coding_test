def solution(dist):
    answer = []

    lens = len(dist[0])

    ele = [i for i in range(lens)]

    temp = []

    check = [False] * lens

    def back(depth):

        nonlocal temp

        if depth == lens:
            answer.append(temp)
            temp = []
            return

        for i in range(lens):
            if check[i]:
                continue

            temp.append(ele[i])
            print(temp)
            check[i] = True
            back(depth + 1)
            check[i] = False
            temp.pop()
    back(0)


    print(answer)
    return answer

dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
solution(dist)
