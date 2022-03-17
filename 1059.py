a = int(input())

arr = list(map(int, input().split()))

b = int(input())


answer1 = 0
answer2 = 0

for i in range(a):
    if arr[i] <= b <= arr[i+1]:
        for k in range(b - arr[i]):
            answer1 += arr[i+1] - arr[i] + k - 1

        answer2 += arr[i + 1] - b -1
print(answer1 + answer2)