n = int(input())

arr = [
    ['***'],
    ['* *'],
    ['***']
]

def writeRow(n): # 3, 9, 27
    skiparr = []
    start = n//3 + 1 # 2 4 10
    ends = n//3+n//3 # 2 6 18
    for j in range(start, ends):
        skiparr.append(j)

    for j in range(n):
        if j in skiparr:
            pass
        else:
            for i in range(3):
                print(arr[i][0], end = "\n")


def writeCol(n):
    n = n//3
    for i in range(n):
        writeRow(n)


writeCol(n)
#writeRow(n)


# 1  2  3 -> 9
# 1 2 3  4 5 6  7 8 9 ->27/3 level, 크게 3묶음 거기서 가운데가 빵구
# 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 18  19 20 21 22 23 24 25 26 27 ->  27 81/3

# k = 1 -> 3 -> 2
# k = 2 -> 9 ->