n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

first = arr[0]
arr = arr[1:]

answer = 0
if len(arr) == 0:
    print(0)
    exit()

while True:
    bef = max(arr)

    if first <= max(arr):
        first += 1
        k = arr.index(bef)
        arr[k] -= 1
        answer += 1

    if first > max(arr):
        break

print(answer)

