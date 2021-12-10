a, b, = map(int, input().split())
arr = [] # 정답 누적
def back(depth):
    if depth == b:
        print(' '.join(map(str, arr)))
        return
    for j in range(1, a+1):
        if j not in arr:
            arr.append(j)
            back(depth + 1)
            arr.pop()
back(0)

