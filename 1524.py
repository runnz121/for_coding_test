t = int(input())

while t > 0:
    x = str(input())
    a, b = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    arrA.sort()
    arrB.sort()

    while True:
        if arrA[0] < arrB[0]:
            arrA.pop(0)
        elif arrA[0] >= arrB[0]:
            arrB.pop(0)

        if len(arrA) == 0:
            print("B")
            break
        elif len(arrB) == 0:
            print("S")
            break
    t -= 1