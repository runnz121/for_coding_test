count = int(input())
arr = []
check = []

for i in range(count):
    arr.append(str(input()))

count = 0
for i in range(len(arr)):#happy
    flag = 1
    check = []
    for j in range(len(arr[i])):# h a p p y
        if arr[i][j] not in check:
            check.append(arr[i][j])
        elif arr[i][j] in check:
            if arr[i][j-1] != arr[i][j]:
                flag = -1
                break
            else:
                flag = 1
    if flag == 1:
        count += 1
print(count)

#예외 : aabbccbb(뒤에도 2개가 나온 경우 flag가 다시 변경)