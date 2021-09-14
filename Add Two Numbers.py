a, b = map(int, input().split())

arr = [i for i in range(1, a+1)]


answer = []
index = 0

for i in range(a):
    index += b-1
    if index >= len(arr):
        index = index%len(arr)
    print(index)
    print("len(arr)",len(arr))

    answer.append(str(arr.pop(index)))

print("<",", ".join(answer)[:], ">", sep='')