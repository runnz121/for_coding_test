x = str(input())

x = list(x)
front = 0
end = len(x) - 1
while True:

    if x[front] != x[end]:
        print(0)
        break
    front += 1
    end -= 1

    if front > end:
        print(1)
        break