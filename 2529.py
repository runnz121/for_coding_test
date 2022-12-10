n = int(input())
x = list(map(str, input().split()))

nums_min = [i for i in range(10)]
nums_max = [i for i in range(10,-1, -1)]

check_min = [False * ]

min_arr = []
tmp1 = []
def back(depth):

    global min_arr
    global tmp1

    if depth == n:
        min_arr.append(tmp1)
        return

    for i in range(n):
