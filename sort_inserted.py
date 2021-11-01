array = [7,5,9,4,3,1,6,2,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        #print(j)
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            print(array)
        else:
            break
print(array)