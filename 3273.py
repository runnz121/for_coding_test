import sys
input = sys.stdin.readline
x = int(input())
arr = list(map(int, input().split()))
find = int(input())

arr.sort()
count = 0
start = 0
end = 1
while start < x:
    if end == x:
        if start == x-1:
            break
        else:
            start += 1
            end = start + 1
            if end == x:
                break

    res = arr[start] + arr[end]

    if res < find:
        end += 1
    elif res > find:
        start += 1
        end = start + 1
    elif res == find:
        count += 1
        end += 1

print(count)