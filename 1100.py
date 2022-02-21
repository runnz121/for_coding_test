arr = []

for i in range(8):
    arr.append(list(map(str, input())))
arr.reverse()
count = 0
for i in range(8):
    for j in range(8):
        if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
            if arr[i][j] == 'F':
                count += 1

print(count)