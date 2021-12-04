array = [1,3,2,7,8,6,15]
new_array = []
length = 0
for i in range(len(array)):
    if new_array[-1] < array[i]:
        new_array.append(i)
        length += 1

