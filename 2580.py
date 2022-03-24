arr = []
rest = []

for i in range(10):
    num = map(int, input().split())
    arr.append(list(num))

for i in range(9):
    row = arr[i]
    rest = []
    for j in range(1, 10):
        if j not in row:
            rest.append(j)