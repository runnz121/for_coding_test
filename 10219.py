t = int(input())

while t:

    a, b = map(int, input().split())

    graph = []
    answer = []

    for i in range(a):
        graph.append(list(str(input())))

    for i in graph:
        answer.append(i[::-1])


    for k in answer:
        print("".join(k))

    t -= 1


