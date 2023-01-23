n = int(input())
array = list(map(int, input().split()))
array.sort()

num = 1

for i in array:
    if num < i:
        break
    num += i

print(num)