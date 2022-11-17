arr = list(str(input()))

answer = ""

answer = arr[0]

for i in range(len(arr)):
    if arr[i] =='-':
        answer += arr[i + 1]

print(answer)