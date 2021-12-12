arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

def check(row,col):
    checkrow = []
    checkcol = []
    for i in range(9):
        checkrow.append(arr[row][i])
        checkcol.append(arr[i][col])
        print(checkrow, checkcol)
        for j in range(1,9):
            if j not in checkrow and j not in checkcol:
                return j


#a = row, b= col
for row in range(9):
    for col in range(9):
        if arr[row][col] == 0:
            arr[row][col] = check(row, col)

print(arr)