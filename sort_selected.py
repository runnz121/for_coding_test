array = [7,5,9,4,3,1,6,2,8]

for i in range(len(array)):
    minv = i
    #print(minv)
    for j in range(i+1, len(array)):
        if array[minv] > array[j]:
            minv = j
            #print(minv)
    array[i], array[minv] = array[minv], array[i]
    print(array)

print(array)