a, b = map(int, input().split())
arr = []

def back(depth):
    if depth == b:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, a + 1):
        if len(arr) >= 1 and arr[depth-1] <= i:
            arr.append(i)
            back(depth + 1)
            arr.pop()
        elif len(arr) == 0:
            arr.append(i)
            back(depth + 1)
            arr.pop()
back(0)